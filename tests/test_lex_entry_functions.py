import pytest
from Model.lexentry import *


def test_process_text():
    lex_entry = LexEntry(
        form="Test, text!",
        pos="NOUN",         # Provide a dummy POS value
        gloss="A test entry"  # Provide a dummy gloss value
    )
    processed_text = lex_entry.process_text("Test, text!")
    assert processed_text == "test text"  # Adjust expected result as needed


def test_get_words():
    lex_entry = LexEntry(
        form="Hello, world!",
        pos="NOUN",         # Provide a dummy POS value
        gloss="A greeting",  # Provide a dummy gloss value
        sentence="Hello world."
    )
    words = lex_entry.get_words()
    assert words == ["Hello", "world"]  # Adjust expected result as needed
