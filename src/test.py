# import unittest  
# from unittest.mock import patch, MagicMock  
# from google_meet_bot import GoogleMeetBot  

# class TestGoogleMeetBot(unittest.TestCase):  

#     @patch('google_meet_bot.setup_driver')  
#     @patch('google_meet_bot.Authenticator')  
#     @patch('google_meet_bot.MeetControls')  
#     @patch('google_meet_bot.SubtitleSaver')  
#     @patch('google_meet_bot.TextTranslator')  
#     @patch('google_meet_bot.QuestionChecker')  
#     @patch('google_meet_bot.AIResponse')  
#     def setUp(self, mock_ai_response, mock_question_checker, mock_text_translator,   
#                mock_subtitle_saver, mock_meet_controls, mock_authenticator,   
#                mock_setup_driver):  
#         # Mocking the setup for GoogleMeetBot  
#         self.mock_driver = MagicMock()  
#         mock_setup_driver.return_value = self.mock_driver  
#         self.bot = GoogleMeetBot(  
#             email='test@example.com',  
#             password='password123',  
#             api_key='fake_api_key',  
#             ai_api_key='fake_ai_api_key',  
#             update_signal=MagicMock()  
#         )  
#         self.bot.authenticator = mock_authenticator.return_value  
#         self.bot.controls = mock_meet_controls.return_value  
#         self.bot.subtitle_saver = mock_subtitle_saver.return_value  
#         self.bot.translator = mock_text_translator.return_value  
#         self.bot.question_checker = mock_question_checker.return_value  
#         self.bot.ai_response = mock_ai_response.return_value  

#     def test_login(self):  
#         # Test that the login method calls the Authenticator's login method  
#         self.bot.login()  
#         self.bot.authenticator.login.assert_called_once()  

#     def test_turn_off_mic_cam(self):  
#         # Test that the turn_off_mic_cam method calls the MeetControls method  
#         self.bot.turn_off_mic_cam()  
#         self.bot.controls.turn_off_mic_cam.assert_called_once()  

#     @patch('google_meet_bot.time.sleep', return_value=None)  # Mock sleep to avoid delays  
#     def test_start_meeting(self, mock_sleep):  
#         meeting_link = "https://meet.google.com/test-meeting"  
#         self.bot.start(meeting_link)  
        
#         # Check that the login method is called  
#         self.bot.authenticator.login.assert_called_once()  
        
#         # Check that the driver navigates to the meeting link  
#         self.bot.driver.get.assert_called_with(meeting_link)  
        
#         # Check that the microphone and camera are turned off  
#         self.bot.controls.turn_off_mic_cam.assert_called_once()  
        
#         # Check that the subtitle saver thread is started  
#         self.assertTrue(self.bot.subtitle_saver.save_subtitles.called)  

#     def test_program_termination(self):  
#         # Test that the driver quits when the program is terminated  
#         with self.assertRaises(KeyboardInterrupt):  
#             self.bot.start("https://meet.google.com/test-meeting")  
#         self.bot.driver.quit.assert_called_once()  

# if __name__ == '__main__':  
#     unittest.main()



# 2222222222222222222222222222222222222222222222222222222222222222222222



import unittest  
from unittest.mock import patch, MagicMock  
from google_meet_bot import GoogleMeetBot  
# from translator import TextTranslator
# from TextTranslator import translate_to_french

class TestGoogleMeetBot(unittest.TestCase):  

    @patch('google_meet_bot.setup_driver')  
    @patch('google_meet_bot.Authenticator')  
    @patch('google_meet_bot.MeetControls')  
    @patch('google_meet_bot.SubtitleSaver')  
    @patch('google_meet_bot.TextTranslator')  
    @patch('google_meet_bot.QuestionChecker')  
    @patch('google_meet_bot.AIResponse')  
    def setUp(self, mock_ai_response, mock_question_checker, mock_text_translator,   
               mock_subtitle_saver, mock_meet_controls, mock_authenticator,   
               mock_setup_driver):  
        # Mocking the setup for GoogleMeetBot  
        self.mock_driver = MagicMock()  
        mock_setup_driver.return_value = self.mock_driver  
        self.bot = GoogleMeetBot(  
            email='test@example.com',  
            password='password123',  
            api_key='fake_api_key',  
            ai_api_key='fake_ai_api_key',  
            update_signal=MagicMock()  
        )  
        self.bot.authenticator = mock_authenticator.return_value  
        self.bot.controls = mock_meet_controls.return_value  
        self.bot.subtitle_saver = mock_subtitle_saver.return_value  
        self.bot.translator = mock_text_translator.return_value  
        self.bot.question_checker = mock_question_checker.return_value  
        self.bot.ai_response = mock_ai_response.return_value  

    def test_login(self):  
        # Test that the login method calls the Authenticator's login method  
        self.bot.login()  
        self.bot.authenticator.login.assert_called_once()  

    def test_turn_off_mic_cam(self):  
        # Test that the turn_off_mic_cam method calls the MeetControls method  
        self.bot.turn_off_mic_cam()  
        self.bot.controls.turn_off_mic_cam.assert_called_once()  

    @patch('google_meet_bot.time.sleep', return_value=None)  # Mock sleep to avoid delays  
    def test_start_meeting(self, mock_sleep):  
        meeting_link = "https://meet.google.com/test-meeting"  
        self.bot.start(meeting_link)  
        
        # Check that the login method is called  
        self.bot.authenticator.login.assert_called_once()  
        
        # Check that the driver navigates to the meeting link  
        self.bot.driver.get.assert_called_with(meeting_link)  
        
        # Check that the microphone and camera are turned off  
        self.bot.controls.turn_off_mic_cam.assert_called_once()  
        
        # Check that the subtitle saver thread is started  
        self.assertTrue(self.bot.subtitle_saver.save_subtitles.called)  

    def test_program_termination(self):  
        # Test that the driver quits when the program is terminated  
        with self.assertRaises(KeyboardInterrupt):  
            self.bot.start("https://meet.google.com/test-meeting")  
        self.bot.driver.quit.assert_called_once()  

    def test_subtitle_saving(self):
        # Test subtitle saving functionality based on language
        self.bot.selected_language = "Farsi"
        self.bot.subtitle_saver.save_subtitles = MagicMock()
        self.bot.start("https://meet.google.com/test-meeting")
        self.bot.subtitle_saver.save_subtitles.assert_called_once()
        self.bot.translator.translate_to_french.assert_called_once()

    def test_translator_called(self):
        # Test that the translator is called during the meeting
        self.bot.start("https://meet.google.com/test-meeting")
        self.bot.translator.translate.assert_called()  # Assuming translate method exists

    def test_question_checker_called(self):
        # Test that the question checker is called during the meeting
        self.bot.start("https://meet.google.com/test-meeting")
        self.bot.question_checker.check_question.assert_called()  # Assuming check_question method exists

    @patch('google_meet_bot.time.sleep', return_value=None)  # Mock sleep to avoid delays
    def test_login_failure(self, mock_sleep):
        # Simulate a login failure
        self.bot.authenticator.login.side_effect = Exception("Login failed")
        with self.assertRaises(Exception) as context:
            self.bot.start("https://meet.google.com/test-meeting")
        self.assertEqual(str(context.exception), "Login failed")

if __name__ == '__main__':  
    unittest.main()