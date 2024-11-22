# controls.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class MeetControls:
    def __init__(self, driver):
        self.driver = driver

    def turn_off_mic_cam(self):
        try:
            time.sleep(5)
            mic_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "crqnQb", " "))]')))
            mic_button.click()
            print("Microphone turned off.")
        except TimeoutException:
            print("TimeoutException: Element not found or not clickable within specified time.")
        except Exception as e:
            print(f"An error occurred while turning off mic/cam: {e}")
