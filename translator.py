# translator.py
from googletrans import Translator

class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, dest='fa'):
        return self.translator.translate(text, dest=dest).text
    
    # def translate2(self, text, dest='fr'):
    #     return self.translator.translate(text, dest=dest).text
    
    # def translate3(self, text, dest='it'):
    #     return self.translator.translate(text, dest=dest).text
    
