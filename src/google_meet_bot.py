# google_meet_bot.py
import time
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from driver_setup import setup_driver
from translator import TextTranslator
from question_checker import QuestionChecker
from AI import AIResponse
from auth import Authenticator  # Import the Authenticator class
from controls import MeetControls  # Import the MeetControls class
from subtitle_saver_fa import SubtitleSaver  # Import the SubtitleSaver class

class GoogleMeetBot:
    def __init__(self, email, password, api_key, ai_api_key, update_signal):
        self.email = email
        self.password = password
        self.api_key = api_key
        self.ai_response = AIResponse(ai_api_key)
        self.driver = setup_driver()
        self.translator = TextTranslator()
        self.question_checker = QuestionChecker(api_key)
        self.authenticator = Authenticator(self.driver, self.email, self.password)
        self.controls = MeetControls(self.driver)  # Initialize MeetControls
        self.subtitle_saver = SubtitleSaver(self.driver, self.translator, self.question_checker, update_signal)
    
    def login(self):
        self.authenticator.login()  # Use the Authenticator class for login

    def turn_off_mic_cam(self):
        self.controls.turn_off_mic_cam()  # Use the MeetControls class for turning off mic/cam

    def start(self, meeting_link):
        self.login()
        self.driver.get(meeting_link)
        self.turn_off_mic_cam()

        subtitle_thread = threading.Thread(target=self.subtitle_saver.save_subtitles, daemon=True)  # Use SubtitleSaver
        subtitle_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program terminated by user.")
        finally:
            self.driver.quit()
