# login_module.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def login(driver, email, password):
    try:
        driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
        
        # Wait for the email input field and enter the email
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "identifierId"))
        )
        email_field.send_keys(email)
        driver.find_element(By.ID, "identifierNext").click()

        # Wait for the password input field and enter the password
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        password_field.send_keys(password)
        driver.find_element(By.ID, "passwordNext").click()

        # Wait until the login is complete by checking for the Google homepage
        WebDriverWait(driver, 10).until(EC.url_contains("google.com"))
        print("Login successful.")
    
    except TimeoutException:
        print("TimeoutException: Unable to locate an element during login.")
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during login: {e}")
