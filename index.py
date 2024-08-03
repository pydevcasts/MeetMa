# # import required modules
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time


# def GoogleMeet(mail_address, password):
#     # Login Page
#     driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

#     # input Gmail
#     driver.find_element(By.ID, "identifierId").send_keys(mail_address)
#     driver.find_element(By.ID, "identifierNext").click()
#     driver.implicitly_wait(10)

#     # input Password
#     driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
#     driver.implicitly_wait(10)
#     driver.find_element(By.ID, "passwordNext").click()
#     driver.implicitly_wait(10)

#     # go to google home page
#     driver.get('https://google.com/')
#     driver.implicitly_wait(100)


# def turnOffMicCam():
#     # turn off Microphone
#     # time.sleep(2)
#     # driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
#     # driver.implicitly_wait(3)

#     # turn off camera
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
#     driver.implicitly_wait(3)


# def joinNow():
#     # Join meet
#     time.sleep(5)
#     driver.implicitly_wait(2)
#     driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
#     print("kosos")

#     # Open a file to save the subtitles
#     with open('subtitles.txt', 'a', encoding='utf-8') as f:
#         while True:
#             try:
#                 # Locate the subtitle element (adjust the XPath as necessary)
#                 subtitles = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "iOzk7", " " ))]')
#                 subtitle_text = subtitles.text
                
#                 if subtitle_text:  # Check if subtitle_text is not empty
#                     f.write(subtitle_text + '\n')
#                     print(subtitle_text)  # Print to console for real-time feedback

            
#             except Exception as e:
#                 print(f"Error: {e}")
#                 break


# mail_address = 'pydevcasts@gmail.com'
# password = 'Poing1981'

# options = Options()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--start-maximized')
# options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.media_stream_camera": 1,
#     "profile.default_content_setting_values.geolocation": 0,
#     "profile.default_content_setting_values.notifications": 1
# })
# driver = webdriver.Chrome(options=options)

# GoogleMeet(mail_address, password)

# driver.get('https://meet.google.com/gkd-esge-uvu')
# turnOffMicCam()
# joinNow()

####################################################################3
# import required modules
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time


# def GoogleMeet(mail_address, password):
#     # Login Page
#     driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

#     # input Gmail
#     driver.find_element(By.ID, "identifierId").send_keys(mail_address)
#     driver.find_element(By.ID, "identifierNext").click()
#     driver.implicitly_wait(10)

#     # input Password
#     driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
#     driver.implicitly_wait(10)
#     driver.find_element(By.ID, "passwordNext").click()
#     driver.implicitly_wait(100)


# def turnOffMicCam():
#     # turn off Microphone
 
#     time.sleep(2)
#     driver.WebDriverWait(3)
#     driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "VYBDae-Bz112c-RLmnJb", " " ))]').click()
#     print(driver,1000000000000000000000000000000000000000000)
#     driver.implicitly_wait(3)

#     # turn off camera
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "HNeRed", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "VYBDae-Bz112c-RLmnJb", " " ))]').click()
#     driver.implicitly_wait(3)


# def joinNow():
#     # Join meet
#     time.sleep(5)
#     driver.implicitly_wait(2)
#     driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
#     # click subtitle 
#     # //*[contains(concat( " ", @class, " " ), concat( " ", "R5ccN", " " ))]//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "VYBDae-Bz112c-RLmnJb", " " ))]
#     with open('subtitles.txt', 'a', encoding='utf-8') as f:
#         while True:
#             try:
#                 # Locate the subtitle element (adjust the XPath as necessary)
#                 subtitles = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "iOzk7", " " ))]')
#                 subtitle_text = subtitles.text
                
#                 if subtitle_text:  # Check if subtitle_text is not empty
#                     f.write(subtitle_text + '\n')
#                     print(subtitle_text)  # Print to console for real-time feedback

            
#             except Exception as e:
#                 print(f"Error: {e}")
#                 break


# mail_address = 'pydevcasts@gmail.com'
# password = 'Poing1981'

# options = Options()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--start-maximized')
# options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.media_stream_camera": 1,
#     "profile.default_content_setting_values.geolocation": 0,
#     "profile.default_content_setting_values.notifications": 1
# })
# driver = webdriver.Chrome(options=options)
# GoogleMeet(mail_address, password)
# driver.get('https://meet.google.com/gkd-esge-uvu')
# turnOffMicCam()
# joinNow()

###############################################################3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def GoogleMeet(mail_address, password):
    # Login Page
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    # input Gmail
    driver.find_element(By.ID, "identifierId").send_keys(mail_address)
    driver.find_element(By.ID, "identifierNext").click()

    # input Password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()

    # Go to Google home page
    WebDriverWait(driver, 10).until(EC.url_contains("google.com"))

# def turnOffMicCam():
    # Turn off Microphone
    # time.sleep(5)  # Wait for the UI to load
    # driver.implicitly_wait(4)
    # mic_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "crqnQb", " " ))]')))
    # print(mic_button, 55555555555555555555555555)
    # mic_button.click()

    # Turn off camera
    # time.sleep(1)
    # driver.implicitly_wait(2)
    # camera_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "VYBDae-Bz112c-RLmnJb", " " ))]')))
    # camera_button.click()

# def joinNow():
#     # Join meet
#     time.sleep(5)
#     join_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt')))
#     join_button.click()
#     print("Joined the meeting")

def save_subtitles():
    # Open a file to save the subtitles
    with open('subtitles.txt', 'a', encoding='utf-8') as f:
        previous_subtitle = ""
        while True:
            try:
                # Locate the subtitle element (adjust the XPath as necessary)
                subtitles = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "crqnQb", " " ))]')))
                print(subtitles, 11111111111111)
                subtitle_text = subtitles.text.strip()

                if subtitle_text and subtitle_text != previous_subtitle:  # Check if subtitle_text is new and not empty
                    f.write(subtitle_text + '\n')
                    print(subtitle_text)  # Print to console for real-time feedback
                    previous_subtitle = subtitle_text  # Update previous subtitle

                time.sleep(2)  # Sleep to avoid overwhelming the output
            
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
# turnOffMicCam()
# joinNow()
save_subtitles()
