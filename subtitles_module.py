# subtitles_module.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from googletrans import Translator




def save_subtitles_real_time(driver, previous_subtitles):
    translator = Translator()
    with open('subtitles.txt', 'a', encoding='utf-8') as f:
        while True:
            try:
                subtitles = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "iOzk7", " "))]')))
                subtitle_text = subtitles.text.strip()
                
                if subtitle_text and subtitle_text not in previous_subtitles:
                    translated_text = translator.translate(subtitle_text, dest='fa').text
                    if translated_text:
                        f.write(f"English: {subtitle_text}\nPersian: {translated_text}\n" + "*" * 40 + '\n')
                    else:
                        print("Translation returned None or unexpected format.")
                    f.flush()
              
                    previous_subtitles.add(subtitle_text)
            except TimeoutException:
                print("TimeoutException: Element not found.")
            except Exception as e:
                print(f"Error: {e}")
                break


# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from googletrans import Translator
# import threading

# # Create a lock for thread safety
# lock = threading.Lock()

# def translate_and_save(subtitle_text, f, previous_subtitles):
#     translator = Translator()
#     translated_text = translator.translate(subtitle_text, dest='fa').text
#     if translated_text:
#         with lock:  # Ensure thread-safe access to shared resources
#             f.write(f"English: {subtitle_text}\nPersian: {translated_text}\n" + "*" * 40 + '\n')
#             f.flush()
#             previous_subtitles.add(subtitle_text)
#     else:
#         print("Translation returned None or unexpected format.")

# def save_subtitles_real_time(driver, previous_subtitles):
#     with open('subtitles.txt', 'a', encoding='utf-8') as f:
#         while True:
#             try:
#                 subtitles = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.XPATH, '//*[contains(concat(" ", @class, " "), concat(" ", "iOzk7", " "))]')))
#                 subtitle_text = subtitles.text.strip()
                
#                 if subtitle_text and subtitle_text not in previous_subtitles:
#                     # Start a new thread for translation and saving
#                     threading.Thread(target=translate_and_save, args=(subtitle_text, f, previous_subtitles), daemon=True).start()
#                     time.sleep(1)  # Delay between saves
                    
#             except TimeoutException:
#                 print("TimeoutException: Element not found.")
#             except Exception as e:
#                 print(f"Error: {e}")
#                 break
