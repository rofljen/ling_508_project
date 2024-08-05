import pytest
from Model.text import Text
from Model.lexentry import LexEntry


def test_lex_entries():
    # Example of how to use LexEntry with different arguments
    text = Text("Hello, this is an example text. It has multiple sentences.")
    sentences = text.split_into_sent()
    for sentence in sentences:
        # Adjust according to actual values you want to test
        lex_entry = LexEntry(form='example_form', pos='NOUN', gloss='example_gloss', sentence=sentence)


def test_lemma():
    text = Text("Hello, this is an example text. It has multiple sentences.")
    sentences = text.split_into_sent()
    for sentence in sentences:
        lex_entry = LexEntry(form='example_form', pos='NOUN', gloss='example_gloss', sentence=sentence)
        # Test lemma functionality with different words
        print(lex_entry.lemmatize_word('example'))
        print(lex_entry.lemmatize_word('texts'))
