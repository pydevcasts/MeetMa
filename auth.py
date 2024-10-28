# auth.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Authenticator:
    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def login(self):
        try:
            self.driver.get('https://accounts.google.com/ServiceLogin')
            self.driver.find_element(By.ID, "identifierId").send_keys(self.email)
            self.driver.find_element(By.ID, "identifierNext").click()

            password_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
            password_field.send_keys(self.password)

            WebDriverWait(self.driver, 10).until(EC.url_contains("google.com"))
            print("Login successful!")
        except Exception as e:
            print(f"Error during login: {e}")
            self.driver.quit()
