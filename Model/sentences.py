import spacy

class Sent:
    def __init__(self, text: str, lang='en'):
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        self.text = text
        self.nlp = spacy.load(self.get_model_name(lang))
        self.sentences = self.split_into_sent()

    def get_model_name(self, lang):
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

    def split_into_sent(self):
        try:
            doc = self.nlp(self.text)
            return [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        except Exception as e:
            print(f"Error during sentence segmentation: {e}")
            return []

    def get_sentence(self, index):
        if index < 0 or index >= len(self.sentences):
            raise IndexError("Index out of range")
        return self.sentences[index]

    def __str__(self):
        return ' '.join(self.sentences)
