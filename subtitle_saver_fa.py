# subtitle_saver.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SubtitleSaver:
    def __init__(self, driver, translator, question_checker, update_signal):
        self.driver = driver
        self.translator = translator
        self.question_checker = question_checker
        self.previous_subtitles = set()
        self.update_signal = update_signal

    def save_subtitles(self):
        with open('subtitles.txt', 'a', encoding='utf-8') as f:
            while True:
                try:
                    subtitles = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "iOzk7", " "))]')))
                    subtitle_text = subtitles.text.strip()

                    if subtitle_text and subtitle_text not in self.previous_subtitles:
                        f.write("English: " + subtitle_text + '\n' + "*" * 20 + '\n')

                        if self.question_checker.is_question(subtitle_text):
                            f.write("Type: Question" + '\n' + "*" * 20 + '\n')
                        else:
                            f.write("Type: Statement" + '\n' + "*" * 20 + '\n')

                        translated_text = self.translator.translate(subtitle_text, dest='fa')
                        f.write("Persian: " + translated_text + '\n' + "*" * 20 + '\n')

                        translated_text2 = self.translator.translate(subtitle_text, dest='fr')
                        f.write("French: " + translated_text2 + '\n' + "*" * 20 + '\n')

                        f.flush()
                        self.update_signal.emit(f"English: {subtitle_text}\nType: {'Question' if self.question_checker.is_question(subtitle_text) else 'Statement'}\nPersian: {translated_text}\n\n French: {translated_text2}")

                        self.previous_subtitles.add(subtitle_text)
                    time.sleep(1)
                except TimeoutException:
                    print("TimeoutException: Element not found.")
                except Exception as e:
                    print(f"Error: {e}")
                    break
