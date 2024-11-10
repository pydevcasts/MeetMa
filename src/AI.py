import requests

class AIResponse:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_ai_answer(self, question):
        url = 'https://api.aimlapi.com/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'text': question
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # will raise an error for 4xx/5xx responses
            result = response.json()
            return result.get('answer', 'AI could not provide an answer.')
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return 'AI API error: Unable to get a response.'
        except Exception as err:
            print(f"Other error occurred: {err}")
            return 'AI API error: Unable to get a response.'
        
















        # pydevcasts@gmail.com
        # Poing1981@
        # https://meet.google.com/ikb-byyj-bui