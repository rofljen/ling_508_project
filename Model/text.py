import spacy
from Model.enums import Lang, Genre
class Text:
    def __init__(self, text: str, text_lang: Lang, text_name: str = None, text_source: str = None, text_genre: str = None, word_count: int = None):
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        self.text = text
        self.text_lang = text_lang
        self.text_name = text_name
        self.text_source = text_source
        self.text_genre = text_genre
        self.word_count = word_count
        self.nlp = spacy.load(self.get_model_name(text_lang))

    def get_model_name(self, lang: Lang) -> str:
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

    def get_genre_from_string(self, genre_str: str) -> Genre:
        genre_mapping = {
            'Non-Fiction': Genre.NON_FICTION,
            'Fiction': Genre.FICTION,
            'News': Genre.NEWS,
            'Science': Genre.SCIENCE
        }
        return genre_mapping.get(genre_str.title(), Genre.NONE)
    def get_lang_from_string(self, lang_str: str) -> Lang:
        lang_mapping = {
            'en': Lang.en,
            'es': Lang.es,
            'de': Lang.de,
            'fr': Lang.fr,
            'it': Lang.it,
            'nl': Lang.nl,
            'pt': Lang.pt,
            'xx': Lang.xx
        }
        return lang_mapping.get(lang_str.lower(), Lang.en)

    def accept_input(self):
        text = input("Please enter your text: ")
        lang_input = input("Please enter the text language (en, es, de, fr, it, nl, pt, xx): ").lower()
        lang = self.get_lang_from_string(lang_input)
        text_name = input("Please provide a name for the text: ")
        text_source = input("Please provide a text source: ")
        genre_input = input("Please provide a text genre (Non-Fiction, Fiction, News, Science): ")
        text_genre = self.get_genre_from_string(genre_input)

        self.text = text
        self.text_lang = lang
        self.text_name = text_name
        self.text_source = text_source
        self.text_genre = text_genre
        self.word_count = len(self.text.split())
        self.nlp = spacy.load(self.get_model_name(self.text_lang))

    def __str__(self):
        return self.text
