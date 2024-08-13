import pytest
from Model.text import Text
from Model.sentences import Sent
from Model.lexentry import LexEntry

def test_text_initialization():
    text = "Hello, this is an example text. It has multiple sentences."
    lang = 'en'

    text_instance = Text(text=text, text_lang=lang)

    assert text_instance.text == text
    assert text_instance.text_lang == lang


def test_sentences():
    text = "Hello, this is an example text. It has multiple sentences."
    lang = 'en'

    sent_instance = Sent(text, lang)  # Create an instance of Sent
    sentences = sent_instance.split_into_sent()  # Call split_into_sent() on the instance

    # Add assertions to verify the sentences
    assert len(sentences) > 0
    assert sentences[0] == "Hello, this is an example text."
def test_lex_entries():
    text = "Hello, this is an example text. It has multiple sentences."
    lang = 'en'

    # Create an instance of Sent
    sent_instance = Sent(text, lang)

    # Call split_into_sent() on the instance
    sentences = sent_instance.split_into_sent()

    # Add your assertions here
    assert len(sentences) > 0
    # Example assertion to check the content of sentences
    assert sentences[0] == "Hello, this is an example text."

