import spacy
class Text:
    def __init__(self, text="", lang="en"):
        self.text = text
        self.lang = lang
        self.nlp = self.load_model(lang)

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

    def split_into_sent(self):
        doc = self.nlp(self.text)
        sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        return sentences

    def __str__(self):
        return self.text
