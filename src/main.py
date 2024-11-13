

import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QLineEdit, QPushButton, QTextEdit, QFileDialog, QComboBox)
from PyQt6.QtCore import QThread, pyqtSignal
import driver_setup
from google_meet_bot import GoogleMeetBot
from subtitle_saver_fr import SubtitleSaverFr
from subtitle_saver_fa import SubtitleSaverFa
from subtitle_saver_ch import SubtitleSaverCh
class MeetingThread(QThread):
    update_output = pyqtSignal(str)

    def __init__(self, email, password, meeting_link, api_key, ai_api_key, translator, question_checker, selected_language):
        super().__init__()
        self.email = email
        self.password = password
        self.meeting_link = meeting_link
        self.api_key = api_key
        self.ai_api_key = ai_api_key
        self.translator = translator
        self.question_checker = question_checker
        self.selected_language = selected_language

    def run(self):
        self.update_output.emit("Starting the meeting...")
        self.bot = GoogleMeetBot(
            self.email,
            self.password,
            self.api_key,
            self.ai_api_key,
            self.update_output,
            self.selected_language
        )
        self.bot.start(self.meeting_link)

        # Subtitle saving based on selected language


        subtitle_saver = None
        if self.selected_language == "Farsi":
            subtitle_saver = SubtitleSaverFa(self.driver, self.translator, self.question_checker, self.update_output)
        elif self.selected_language == "French":
            subtitle_saver = SubtitleSaverFr(self.driver, self.translator, self.question_checker, self.update_output)
        elif self.selected_language == "Chinese":
            subtitle_saver = SubtitleSaverCh(self.driver, self.translator, self.question_checker, self.update_output)

        if subtitle_saver:
            subtitle_saver.save_subtitles()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Meet Bot")
        self.setGeometry(400, 400, 800, 800)

        # Initialize translator and question_checker here
        self.translator = None  # Replace with actual translator
        self.question_checker = None  # Replace with actual question_checker

        layout = QVBoxLayout()

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setFixedHeight(40)
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedHeight(40)
        layout.addWidget(self.password_input)

        self.meeting_link_input = QLineEdit(self)
        self.meeting_link_input.setPlaceholderText("Enter meeting link")
        self.meeting_link_input.setFixedHeight(40)
        layout.addWidget(self.meeting_link_input)

        # Create a QComboBox for selecting subtitle language
        self.language_combo = QComboBox(self)
        self.language_combo.addItems(["Select Language", "Farsi","French", "Chinese"])
        layout.addWidget(self.language_combo)

        self.start_button = QPushButton("Start Meeting", self)
        self.start_button.setStyleSheet("background-color: blue; font-size: 16px;")
        self.start_button.setFixedHeight(40)
        self.start_button.clicked.connect(self.start_meeting)
        layout.addWidget(self.start_button)

        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.output_area.setFixedHeight(400)
        layout.addWidget(self.output_area)

        self.download_button = QPushButton("Download Text File", self)
        self.download_button.setStyleSheet("background-color: green; font-size: 16px;")
        self.download_button.setFixedHeight(40)
        self.download_button.clicked.connect(self.download_file)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def start_meeting(self):
        email = self.email_input.text()
        password = self.password_input.text()
        meeting_link = self.meeting_link_input.text()
        selected_language = self.language_combo.currentText()

        if email and password and meeting_link and selected_language != "Select Language":
            self.meeting_thread = MeetingThread(
                email,
                password,
                meeting_link,
                'YOUR_API_KEY',
                'YOUR_AI_API_KEY',
                self.translator,
                self.question_checker,
                selected_language  # Send the selected language here
            )
            self.meeting_thread.update_output.connect(self.append_output)
            self.meeting_thread.start()
        else:
            self.output_area.append("Please fill in all fields and select a language.")


    def append_output(self, message):
        self.output_area.append(message)

    def download_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.output_area.toPlainText())
            self.output_area.append(f"File saved at {file_name}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())