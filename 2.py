# import time
# import threading
# from config import setup_driver
# from login import login
# from subtitles_module import save_subtitles_real_time, translate_and_save
# from turn_off_mic import turn_off_mic_cam


# class GoogleMeetBot:
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
#         self.driver = setup_driver()  # Use the imported function
#         self.previous_subtitles = set()


#     def start(self, meeting_link):
#         login(self.driver, self.email, self.password) 
#         self.driver.get(meeting_link)
#         turn_off_mic_cam(self.driver)  
#         # save_subtitles_real_time(self.driver, self.previous_subtitles)  # Call the subtitles saving function
        
    

#         subtitle_thread = threading.Thread(target=save_subtitles_real_time, args=(self.driver, self.previous_subtitles), daemon=True)
#         subtitle_thread.start()

       

#         try:
#             while True:
#                 time.sleep(1)
#         except KeyboardInterrupt:
#             print("Program terminated by user.")
#         finally:
#             self.driver.quit()

# if __name__ == "__main__":
#     email = 'pydevcasts@gmail.com'
#     password = 'Poing1981@'
#     meeting_link = 'https://meet.google.com/ury-nijq-ihg?authuser=0'

#     bot = GoogleMeetBot(email, password)
#     bot.start(meeting_link)














import time
import threading
from config import setup_driver
from login import login
from subtitles_module import save_subtitles_real_time
from turn_off_mic import turn_off_mic_cam

class GoogleMeetBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = setup_driver()  # Use the imported function
        self.previous_subtitles = set()

    def start(self, meeting_link):
        login(self.driver, self.email, self.password) 
        self.driver.get(meeting_link)
        turn_off_mic_cam(self.driver)  
        
        subtitle_thread = threading.Thread(target=save_subtitles_real_time, args=(self.driver, self.previous_subtitles), daemon=True)
        subtitle_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program terminated by user.")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    email = 'pydevcasts@gmail.com'
    password = 'Poing1981@'
    meeting_link = 'https://meet.google.com/ury-nijq-ihg?authuser=0'

    bot = GoogleMeetBot(email, password)
    bot.start(meeting_link)
