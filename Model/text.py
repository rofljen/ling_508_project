import spacy
from Model.enums import Lang
class Text:
    def __init__(self, text: str, text_lang: str, text_name: str = None, text_source: str = None, text_genre: str = None, word_count: int = None):
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        self.text = text
        self.text_lang = text_lang
        self.text_name = text_name
        self.text_source = text_source
        self.text_genre = text_genre
        self.word_count = word_count
        self.nlp = spacy.load(self.get_model_name(text_lang))

    def get_model_name(self, lang: str) -> str:
        model_name = {
            'en': 'en_core_web_sm',
            'es': 'es_core_news_sm',
            'de': 'de_core_news_sm',
            'fr': 'fr_core_news_sm',
            'it': 'it_core_news_sm',
            'nl': 'nl_core_news_sm',
            'pt': 'pt_core_news_sm',
            'xx': 'xx_ent_wiki_sm'
        }
        return model_name.get(lang, 'en_core_web_sm')

    def accept_input(self):
        self.text = input("Please enter your text: ")
        self.lang = input("Please enter the text language: ")
        self.text_name = input("Please provide a name for the text: ")
        self.text_source = input("Please provide a text source :")
        self.text_genre = input("Please provide a text genre: ")
        self.word_count = len(self.text.split())

        self.nlp = self.load_model(self.text_lang)

    def split_into_sent(self):
        if not isinstance(self.text, str):
            raise ValueError("Text must be a string")
        doc = self.nlp(self.text)
        sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        return sentences

    def __str__(self):
        return self.text
