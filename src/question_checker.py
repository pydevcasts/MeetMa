# question_checker.py
import requests

class QuestionChecker:
    def __init__(self, api_key):
        self.api_key = api_key

    def is_question(self, text):
        wh_question_detected = self.contains_wh_question(text)
        if wh_question_detected:
            return True

        url = 'https://api.aimlapi.com/v1/chat/completions'  # Replace with your API endpoint
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'text': text
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result.get('is_question', False)
        else:
            print(f"API error: {response.status_code}, Message: {response.text}")
            return False

    def contains_wh_question(self, text):
        wh_words = ['who', 'what', 'where', 'when', 'why', 'which']
        text_lower = text.lower()
        return any(wh in text_lower for wh in wh_words)
