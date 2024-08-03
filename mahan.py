from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

def GoogleMeet(mail_address, password):
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
    driver.find_element(By.ID, "identifierId").send_keys(mail_address)
    driver.find_element(By.ID, "identifierNext").click()
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    password_field.send_keys(password)
    WebDriverWait(driver, 10).until(EC.url_contains("google.com"))

def turnOffMicCam():
    try:
        time.sleep(5)  # Wait for the UI to load
        mic_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "crqnQb", " " ))]')))
        mic_button.click()
    except TimeoutException as e:
        print("TimeoutException: Element not found or not clickable within specified time.")
    except Exception as e:
        print(f"An error occurred: {e}")



def save_subtitles():
    with open('subtitles.txt', 'a', encoding='utf-8') as f:
        previous_subtitle = ""
        while True:
            try:
                subtitles = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "iOzk7", " " ))]')))
                subtitle_text = subtitles.text.strip()
                if subtitle_text and subtitle_text != previous_subtitle: 
                    f.write(subtitle_text + '\n')
                    print(subtitle_text) 
                    previous_subtitle = subtitle_text 

                time.sleep(2)  
            
            except TimeoutException as te:
                print(f"TimeoutException: {te}")
            except Exception as e:
                print(f"Error: {e}")
                break
mail_address = 'pydevcasts@gmail.com'
password = 'Poing1981@'

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=options)

GoogleMeet(mail_address, password)

driver.get('https://meet.google.com/gkd-esge-uvu')
turnOffMicCam()
save_subtitles()