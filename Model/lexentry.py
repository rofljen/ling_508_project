import spacy
import string
from nltk.corpus import wordnet


class LexEntry:
    def __init__(self, form, pos, gloss, lemma=None, example=None, sentence=None, lang='en'):
        self.sentence = sentence
        self.pos = pos
        self.gloss = gloss
        self.lemma = lemma
        self.example = example

        if sentence:
            self.nlp = spacy.load(self.get_model_name(lang))
            self.doc = self.nlp(sentence)
        else:
            self.nlp = None
            self.doc = None

        self.form = self.process_text(form).split()

    def get_model_name(self, lang):
        model_name = {
            'nl': "nl_core_news_lg",
            'en': "en_core_web_trf",
            'fr': "fr_dep_news_trf",
            'de': "de_dep_news_trf",
            'it': "it_core_news_lg",
            'xx': "xx_sent_ud_sm",
            'pt': "pt_core_news_lg",
            'es': "es_dep_news_trf"
        }.get(lang, 'en_core_web_trf')  # Default to English if language not found

        return model_name

    def process_text(self, text):
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator)
        return cleaned_text.lower()

    def get_words(self):
        if self.nlp and self.doc:
            return [token.text for token in self.doc if not token.is_punct]
        return []

    def return_lex_entries(self):
        if self.nlp:
            return [token.text.lower() for token in self.doc if token.text not in string.punctuation]
        return []

    def get_word_len(self):
        return [len(word) for word in self.return_lex_entries()]

    def get_word_index(self, word):
        lex_entries = self.return_lex_entries()
        try:
            return lex_entries.index(word)
        except ValueError:
            return -1

    def get_pos(self, word):
        if self.nlp:
            doc = self.nlp(word)
            return doc[0].pos_
        return None

    def lemmatize_word(self, word):
        if self.nlp:
            doc = self.nlp(word)
            return doc[0].lemma_
        return word

    def get_gloss(self, word):
        synsets = wordnet.synsets(word)
        glosses = {}
        for synset in synsets:
            glosses[synset.name()] = {
                'definition': synset.definition(),
                'examples': synset.examples()
            }
        return glosses

    def get_word_details(self, word):
        if self.nlp:
            doc = self.nlp(word)
            word_info = {
                'form': word,
                'POS': doc[0].pos_,
                'lemma': doc[0].lemma_,
                'gloss': self.get_gloss(word)
            }
            return word_info
        return {}
