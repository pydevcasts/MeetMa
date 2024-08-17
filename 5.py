import time
import threading
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from googletrans import Translator
from AI import AIResponse



class GoogleMeetBot:
    def __init__(self, email, password, api_key, ai_api_key):
        self.email = email
        self.password = password
        self.api_key = api_key
        self.ai_response = AIResponse(ai_api_key)  # Create an instance of AIResponse with AI API key        self.driver = self.setup_driver()
        self.driver = self.setup_driver()
        self.previous_subtitles = set()
        self.translator = Translator()

    def setup_driver(self):
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--start-maximized')
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1
        })
        return webdriver.Chrome(options=options)

    def login(self):
        try:
            self.driver.get('https://accounts.google.com/ServiceLogin')
            self.driver.find_element(By.ID, "identifierId").send_keys(self.email)
            self.driver.find_element(By.ID, "identifierNext").click()

            # Wait for password input field to be clickable and input password
            password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
            password_field.send_keys(self.password)

            # Confirm we are logged in by waiting for a known element
            WebDriverWait(self.driver, 10).until(EC.url_contains("google.com"))
            print("Login successful!")
        except Exception as e:
            print(f"Error during login: {e}")
            self.driver.quit()

    def turn_off_mic_cam(self):
        try:
            time.sleep(5)  # Wait for the UI to load
            mic_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "crqnQb", " "))]')))
            mic_button.click()
        except TimeoutException:
            print("TimeoutException: Element not found or not clickable within specified time.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def is_question(self, text):
        # Check for wh-questions
        wh_question_detected = self.contains_wh_question(text)
        if wh_question_detected:
            return True

        # Call external API to check if it's a question
        url = 'https://api.aimlapi.com/v1/chat/completions'  # Replace with your API endpoint
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'text': text
        }
        response = requests.post(url, headers=headers, json=payload)
        print(f"Requesting: {payload}")
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {result}")
            return result.get('is_question', False)
        else:
            print(f"API error: {response.status_code}, Message: {response.text}")
            return False
    
    def contains_wh_question(self, text):
        # List of wh-words to recognize
        wh_words = ['who', 'what', 'where', 'when', 'why', 'which']
        text_lower = text.lower()
        return any(wh in text_lower for wh in wh_words)
    

    def save_subtitles_real_time(self):
        with open('subtitles.txt', 'a', encoding='utf-8') as f:
            while True:
                try:
                    subtitles = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "iOzk7", " "))]')))
                    subtitle_text = subtitles.text.strip()

                    if subtitle_text and subtitle_text not in self.previous_subtitles:
                        # Write the original English subtitle
                        f.write("English: " + subtitle_text + '\n' + "*" * 40 + '\n')

                        # Check if it is a question
                        if self.is_question(subtitle_text):
                            f.write("Type: Question" + "*" * 40 + '\n')
                        else:
                            f.write("Type: Statement" + "*" * 40 + '\n')

                        # Translate the subtitle to Persian
                        translated_text = self.translator.translate(subtitle_text, dest='fa').text
                        f.write("Persian: " + translated_text + '\n' + "*" * 40 + '\n')

                        f.flush()
                        print("*" * 30)
                        print("English: ", subtitle_text)
                        print("Type: Question" if self.is_question(subtitle_text) else "Type: Statement")
                        print("Persian: ", translated_text)
                        print("#" * 30)

                        self.previous_subtitles.add(subtitle_text)
                    time.sleep(1)
                except TimeoutException:
                    print("TimeoutException: Element not found.")
                except Exception as e:
                    print(f"Error: {e}")
                    break
        if self.is_question(subtitle_text):
            ai_answer = self.ai_response.get_ai_answer(subtitle_text)
            f.write("AI Answer: " + ai_answer + "*" * 40 + '\n')
    def start(self, meeting_link):
        self.login()
        self.driver.get(meeting_link)
        self.turn_off_mic_cam()

        subtitle_thread = threading.Thread(target=self.save_subtitles_real_time, daemon=True)
        subtitle_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program terminated by user.")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    email = 'pydevcasts@gmail.com'
    password = 'Poing1981@'
    api_key = '3467ba5d6f9e4880bd6567366828abf0'
    ai_api_key = '3467ba5d6f9e4880bd6567366828abf0'
    meeting_link = 'https://meet.google.com/ybq-azee-kss'

    bot = GoogleMeetBot(email, password, api_key, ai_api_key)
    bot.start(meeting_link)