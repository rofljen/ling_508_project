import spacy
import string
import nltk
from nltk.corpus import wordnet

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

class Sent:
    def __init__(self, sentences):
        self.sentences = [sentence for sentence in sentences]

    def get_sentence(self, index):
        if index < 0 or index >= len(self.sentences):
            raise IndexError("Index out of range")
        return self.sentences[index]

    def __str__(self):
        return ' '.join(self.sentences)

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


import spacy
import string
import nltk
from nltk.corpus import wordnet

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

class Sent:
    def __init__(self, sentences):
        self.sentences = [sentence for sentence in sentences]

    def get_sentence(self, index):
        if index < 0 or index >= len(self.sentences):
            raise IndexError("Index out of range")
        return self.sentences[index]

    def __str__(self):
        return ' '.join(self.sentences)

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


if __name__ == "__main__":
    lang = input("Please enter the language code")
    text_input = Text(lang=lang)
    text_input = Text()
    text_input.accept_input()
    sentences = text_input.split_into_sent()
    print("Sentences:", sentences)

    sent = Sent(sentences)

    for i, sentence in enumerate(sentences):
        print(f"\nAnalyzing Sentence {i}: {sentence}")
        lex_entry = LexEntry(sentence)
        print("Words in the sentence:", lex_entry.split_into_words())
        print("Word lengths:", lex_entry.get_word_len())
        for word in lex_entry.split_into_words():
            print(f"Word: {word}")
            print(f"Index of the word: {lex_entry.get_word_index(word)}")
            print(f"POS of the word: {lex_entry.get_pos(word)}")
            print(f"Lemmatized form of the word: {lex_entry.lemmatize_word(word)}")
            print(f"Sense of the word: {lex_entry.get_sense(word)}")