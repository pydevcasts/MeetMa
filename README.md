# Google Meet Bot

## Overview
The Google Meet Bot is a Python application designed to automate participation in Google Meet meetings. It integrates various functionalities such as real-time subtitle extraction, translation, and question detection, making it a powerful tool for users who want to enhance their online meeting experience.

## Features

1. **User Authentication**:
   - Allows users to log in to their Google account using their email and password.

2. **Meeting Management**:
   - Users can enter a Google Meet link to join meetings directly from the application.

3. **Real-time Subtitle Capture**:
   - The bot captures subtitles displayed in Google Meet in real-time and saves them to a text file.
   - Subtitles are categorized as either statements or questions.

4. **Translation Services**:
   - Captured English subtitles are translated into Persian (Farsi) using the Google Translate API.
   - Both original and translated subtitles are saved in the output file.

5. **Question Detection**:
   - The application can identify whether a subtitle is a question or a statement using a custom QuestionChecker class.
   - This feature can help users focus on important queries during meetings.

6. **Output Display**:
   - Provides a graphical interface where users can see real-time updates of the subtitles, their types, and translations.
   - Users can download the captured subtitles as a text file for later reference.

7. **Threading for Performance**:
   - Utilizes threading to run subtitle capturing and translation concurrently, ensuring smooth operation without freezing the user interface.

8. **Error Handling**:
   - Implements error handling for various exceptions, including timeouts when waiting for subtitles.

## Technologies Used
- **PyQt6**: For creating the graphical user interface.
- **Selenium**: For automating the web browser to interact with Google Meet.
- **Google Translate API**: For translating subtitles into Persian.
- **Custom Classes**: 
  - `Authenticator` for handling login.
  - `MeetControls` for managing microphone and camera settings.
  - `SubtitleSaver` for capturing and saving subtitles.

## How to Use
1. Clone the repository.
2. Install the required dependencies.
3. Set up your Google credentials and API keys.
4. Run the application and enter your login details and meeting link.
5. Start the meeting to begin capturing and translating subtitles.

## Conclusion
This Google Meet Bot is a versatile tool for anyone looking to improve their online meeting experience by automating subtitle capture and translation. It is particularly useful for non-English speakers or those who wish to keep a record of meeting discussions.

## Select Options

Made a Combo_Box By Pyqt6 
Made Modules For Each Langauge 
Adding Each One, On By One To The Main File Where I Created Combo_Box By PyQt6