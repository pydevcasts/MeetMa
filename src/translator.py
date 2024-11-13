# translator.py
from googletrans import Translator

class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, dest='fa'):
        """Translate text to the specified destination language."""
        return self.translator.translate(text, dest=dest).text

    def translate_to_french(self, text):
        """Translate text to French."""
        return self.translate(text, dest='fr')

    def translate_to_chinese(self, text):
        """Translate text to Chinese (Traditional)."""
        return self.translate(text, dest='zh-TW')
    def is_question(self, text):
        # Simple check to see if the text is a question
        return text.strip().endswith('?')