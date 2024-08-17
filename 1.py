import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from googletrans import Translator

class GoogleMeetBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
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
        self.driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
        self.driver.find_element(By.ID, "identifierId").send_keys(self.email)
        self.driver.find_element(By.ID, "identifierNext").click()

        try:
            # Wait for the password field to be visible
            password_field = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
            password_field.send_keys(self.password)
            
            # Wait for the next button to be clickable
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "passwordNext"))).click()
            
            # Wait for the URL to contain google.com
            WebDriverWait(self.driver, 10).until(EC.url_contains("google.com"))
        except TimeoutException:
            print("TimeoutException: Unable to find the password field.")
        except Exception as e:
            print(f"An error occurred during login: {e}")


    def turn_off_mic_cam(self):
        try:
            time.sleep(0.5)  # Wait for the UI to load
            mic_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "crqnQb", " "))]')))
            mic_button.click()
        except TimeoutException:
            print("TimeoutException: Element not found or not clickable within specified time.")
        except Exception as e:
            print(f"An error occurred: {e}")

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
                        
                        # Translate the subtitle to Persian
                        translated_text = self.translator.translate(subtitle_text, dest='fa').text
                        if translated_text:
                            f.write("Persian: " + translated_text + '\n' + "*" * 40 + '\n')
                        else:
                            print("Translation returned None or unexpected format.")
                        f.flush()
                        # print("*" * 30)
                        # print("English: ", subtitle_text)
                        # print("Persian: ", translated_text)
                        # print("#" * 30)
                        f.write(f"English: {subtitle_text}\nPersian: {translated_text}\n" + "*" * 40 + '\n')
                        print(f"English: {subtitle_text}\nPersian: {translated_text}\n" + "#" * 30)
                        
                        self.previous_subtitles.add(subtitle_text)
                    time.sleep(0.5)
                except TimeoutException:
                    print("TimeoutException: Element not found.")
                except Exception as e:
                    print(f"Error: {e}")
                    break

    def start(self, meeting_link):
        self.login()
        self.driver.get(meeting_link)
        self.turn_off_mic_cam()

        subtitle_thread = threading.Thread(target=self.save_subtitles_real_time, daemon=True)
        subtitle_thread.start()

        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("Program terminated by user.")
        finally:
            self.driver.quit()



if __name__ == "__main__":
    email = 'pydevcasts@gmail.com'
    password = 'Poing1981@'
    meeting_link = 'https://meet.google.com/ybq-azee-kss'

    bot = GoogleMeetBot(email, password)
    bot.start(meeting_link)