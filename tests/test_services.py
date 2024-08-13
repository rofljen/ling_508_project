import pytest
from Model.lexentry import LexEntry
from Model.text import Text
from Model.sentences import Sent
from Web.services import Services


@pytest.fixture
def service():
    return Services()


def test_add_text(service):
    text = "Hello, this is an example text. It has multiple sentences."
    text_name = "Test text"
    text_source = "test source"
    text_lang = "en"
    text_genre = "test genre"

    text_id = service.add_text(text, text_name, text_source, text_lang, text_genre)

    print(text_id)
    assert len(text) >0
    assert text_name == "Test text"
    assert text_genre is not None
    print(text_lang)


def test_add_words_from_text(service):
    text = "Hello, this is an example text. It has multiple sentences."
    lang = "en"

    text_id = service.add_text(text, "Test Text", "test source", lang, "test genre")
    text_instance = Text(text=text, text_lang=lang)
    sent_instance = Sent(text, lang)  # Create an instance of Sent

    sentences = sent_instance.split_into_sent()  # Call split_into_sent() on the instance

    for sentence in sentences:
        lex_entry = LexEntry(
            form='example_form',
            pos='NOUN',
            gloss='example_gloss',
            sentence=sentence
        )

        # Print statements to output results
        print(f"Sentence: {sentence}")
        print(f"Lemmatized 'testing': {lex_entry.lemmatize_word('testing')}")
        print(f"Lemmatized 'texts': {lex_entry.lemmatize_word('texts')}")
        print(f"Part of speech - testing: {lex_entry.get_pos('testing')}")
        print(f"Part of speech - texts: {lex_entry.get_pos('texts')}")
        print(f"Gloss - testing: {lex_entry.get_gloss('testing')}")

