# mic_cam_module.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def turn_off_mic_cam(driver):
    try:
        time.sleep(5)  # Wait for the UI to load
        mic_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "crqnQb", " "))]')))
        mic_button.click()
        print("Microphone and camera turned off.")
    except TimeoutException:
        print("TimeoutException: Element not found or not clickable within specified time.")
    except Exception as e:
        print(f"An error occurred: {e}")
