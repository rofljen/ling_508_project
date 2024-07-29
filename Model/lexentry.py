import spacy
import string
import nltk
from nltk.corpus import wordnet
class LexEntry:


    def __init__(self, sentence, lang='en'):
        self.nlp = spacy.load(self.get_model_name(lang))
        self.doc = self.nlp(sentence)
        self.lex_entries = [token.text.lower() for token in self.doc if token.text not in string.punctuation]

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

    def split_into_words(self):
        return self.lex_entries

    def get_word_len(self):
        return [len(word) for word in self.lex_entries]

    def get_word_index(self, word):
        try:
            return self.lex_entries.index(word)
        except ValueError:
            return -1

    def get_pos(self, word):
        for token in self.doc:
            if token.text == word:
                return token.pos_
        return None

    def lemmatize_word(self, word):
        for token in self.doc:
            if token.text == word:
                return token.lemma_

        return word


    def get_sense(self, word):
        synsets = wordnet.synsets(word)
        senses ={}
        for synset in synsets:
            senses[synset.name()] = {
                'definition': synset.definition(),
                'examples': synset.examples()
            }
        return senses