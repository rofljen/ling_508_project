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

        # Process the form into individual words
        self.form = self.process_text(form).split()

    def get_model_name(self, lang):
        model_name = {
            'en': 'en_core_web_sm',
            'es': 'es_core_news_sm',
            'de': 'de_core_news_sm',
            'fr': 'fr_core_news_sm',
            'it': 'it_core_news_sm',
            'nl': 'nl_core_news_sm',
            'pt': 'pt_core_news_sm',
            'xx': 'xx_ent_wiki_sm'  # Multilingual model
        }.get(lang, 'en_core_web_sm')  # Default to English if language not found

        return model_name

    def process_text(self, text):
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator)
        return cleaned_text.lower()

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
            for token in self.doc:
                if token.text.lower() == word.lower():
                    return token.pos_
        return None

    def lemmatize_word(self, word):
        if self.nlp:
            for token in self.doc:
                if token.text.lower() == word.lower():
                    return token.lemma_
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
