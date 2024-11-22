# subtitle_saver.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from translator import TextTranslator

class SubtitleSaverFa:
    def __init__(self, driver, translator,question_checker, update_signal):
        self.driver = driver
        self.translator = translator
        self.question_checker = question_checker
        self.previous_subtitles = set()
        self.update_signal = update_signal

    def save_subtitles(self):
        with open('subtitles.txt', 'a', encoding='utf-8') as f:
            while True:
                try:
                    subtitle_text = self._get_subtitle_text()
                    if self._is_new_subtitle(subtitle_text):
                        self._write_subtitle_to_file(f, subtitle_text)
                        self.previous_subtitles.add(subtitle_text)
                    time.sleep(1)
                except TimeoutException:
                    print("TimeoutException: Element not found.")
                except Exception as e:
                    print(f"Error: {e}")
                    break

    def _get_subtitle_text(self):
        """Retrieve subtitle text from the web element."""
        subtitles = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "iOzk7", " "))]')))
        return subtitles.text.strip()

    def _is_new_subtitle(self, subtitle_text):
        """Check if the subtitle is new and not previously recorded."""
        return subtitle_text and subtitle_text not in self.previous_subtitles

    def _write_subtitle_to_file(self, f, subtitle_text):
        """Write the subtitle and its translation to the file."""
        f.write("English: " + subtitle_text + '\n' + "*" * 20 + '\n')

        subtitle_type = "Question" if self.question_checker.is_question(subtitle_text) else "Statement"
        f.write(f"Type: {subtitle_type}\n" + "*" * 20 + '\n')

        translated_text = self.translator.translate(subtitle_text, dest='fa')
        f.write("Persian: " + translated_text + '\n' + "*" * 20 + '\n')
        f.flush()

        self.update_signal.emit(f"English: {subtitle_text}\nType: {subtitle_type}\nPersian: {translated_text}\n\n")

