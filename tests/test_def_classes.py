import pytest
from Model.text import Text
from Model.sentences import Sent
from Model.lexentry import LexEntry

def test_sentences():
    text = Text("Hello, this is an example text. It has multiple sentences.")
    sentences = text.split_into_sent()
    sent_chunk = Sent(sentences)

    print("Sentences:")
    for i, sentence in enumerate(sentences):
        print(f"Sentence {i}: {sentence}")

    assert len(sentences) == 2

def test_lex_entries():
    text = Text("Hello, this is an example text. It has multiple sentences.")
    sentences = text.split_into_sent()
    sent_chunk = Sent(sentences)

    pos = "noun"
    gloss = "example gloss"

    expected_forms = [
        ['hello', 'this', 'is', 'an', 'example', 'text'],
        ['it', 'has', 'multiple', 'sentences']
    ]

    for i, sentence in enumerate(sentences):
        form = sentence  # Use the sentence as the form
        lex_entry = LexEntry(form=form, pos=pos, gloss=gloss, sentence=sentence)
        assert lex_entry.sentence == sentence
        assert lex_entry.form == expected_forms[i]
        assert lex_entry.pos == pos
        assert lex_entry.gloss == gloss

def test_lemma():
    text = Text("Hello, this is an example text. It has multiple sentences.")
    sentences = text.split_into_sent()
    sent = Sent(sentences)

    pos = "noun"  # Placeholder POS tag
    gloss = "example gloss"  # Placeholder gloss

    for sentence in sentences:
        lex_entry = LexEntry(form=sentence, pos=pos, gloss=gloss, sentence=sentence)
        assert lex_entry.sentence == sentence
        assert lex_entry.lemmatize_word("text") == "text"
