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
from auth import Authenticator
from controls import MeetControls
from subtitle_saver_fa import SubtitleSaverFa
from subtitle_saver_fr import SubtitleSaverFr
from subtitle_saver_ch import SubtitleSaverCh

class GoogleMeetBot:
    def __init__(self, email, password, api_key, ai_api_key, update_signal, selected_language):
        self.email = email
        self.password = password
        self.api_key = api_key
        self.ai_response = AIResponse(ai_api_key)
        self.driver = setup_driver()
        self.translator = TextTranslator()
        self.question_checker = QuestionChecker(api_key)
        self.authenticator = Authenticator(self.driver, self.email, self.password)
        self.controls = MeetControls(self.driver)
        
        # Initialize the subtitle saver based on the selected language
        if selected_language == "Farsi":
            self.subtitle_saver = SubtitleSaverFa(self.driver, self.translator, self.question_checker, update_signal)
        elif selected_language == "French":
            self.subtitle_saver = SubtitleSaverFr(self.driver, self.translator, self.question_checker, update_signal)
        elif selected_language == "Chinese":
            self.subtitle_saver = SubtitleSaverCh(self.driver, self.translator, self.question_checker, update_signal)

    def login(self):
        """Log in to Google Meet using the Authenticator class."""
        self.authenticator.login()

    def turn_off_mic_cam(self):
        """Turn off microphone and camera using the MeetControls class."""
        self.controls.turn_off_mic_cam()

    def start(self, meeting_link):
        """Start the Google Meet session."""
        self.login()
        self.driver.get(meeting_link)
        self.turn_off_mic_cam()

        # Start the subtitle saver in a separate thread
        subtitle_thread = threading.Thread(target=self.subtitle_saver.save_subtitles, daemon=True)
        subtitle_thread.start()

        try:
            self._keep_running()
        except KeyboardInterrupt:
            print("Program terminated by user.")
        finally:
            self.driver.quit()

    def _keep_running(self):
        """Keep the bot running until interrupted."""
        while True:
            time.sleep(1)
