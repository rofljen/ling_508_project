import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
import string

class Text:
    def __init__(self, text):
        self.text = text

    def split_into_sent(self):
        sentences = sent_tokenize(self.text)
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
    wnl = WordNetLemmatizer()

    pos = {"noun", "pronoun", "verb", "adjective", "adverb", "preposition", "determiner", "conjunction",
           "interjection", }

    def __init__(self, sentence):
        self.wnl = WordNetLemmatizer()
        self.lex_entries = self.process_text(sentence).split()

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
        tag = pos_tag([word])[0][1]
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # Default to noun if not found

    def lemmatize_word(self, word):
        pos = self.get_pos(word)
        return self.wnl.lemmatize(word, pos)

text = Text("Hello world. This is a test sentence.")
sentences = text.split_into_sent()
print(sentences)

sent = Sent(sentences)
print(sent.get_sentence(1))

lex_entry = LexEntry(sent.get_sentence(1))
print(lex_entry.split_into_words())
print(lex_entry.get_word_len())
print(lex_entry.get_word_index("test"))
print(lex_entry.lemmatize_word("favoring"))