import spacy
class Text:
    def __init__(self, text="", text_name="", text_source="", text_lang="en", text_genre="", word_count=0):
        self.text = text
        self.text_name = text_name
        self.text_source = text_source
        self.text_lang = text_lang
        self.text_genre = text_genre
        self.word_count = word_count
        self.nlp = self.load_model(text_lang)

    def load_model(self, lang):
        model_name = {
            'en': 'en_core_web_sm',
            'es': 'es_core_news_sm',
            'de': 'de_core_news_sm',
            'fr': 'fr_core_news_sm',
            'it': 'it_core_news_sm',
            'nl': 'nl_core_news_sm',
            'pt': 'pt_core_news_sm',
            'xx': 'xx_ent_wiki_sm'  # Multilingual model
        }.get(lang, 'en_core_web_sm')

        return spacy.load(model_name)

    def accept_input(self):
        self.text = input("Please enter your text: ")
        self.lang = input("Please enter the text language: ")
        self.text_name = input("Please provide a name for the text: ")
        self.text_source = input("Please provide a text source :")
        self.text_genre = input("Please provide a text genre: ")
        self.word_count = len(self.text.split())

    def split_into_sent(self):
        doc = self.nlp(self.text)
        sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        return sentences

    def __str__(self):
        return self.text
