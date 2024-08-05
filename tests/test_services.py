import pytest
from app.services import Services
from db.mysql_repository import MysqlRepository


# Use a fixture to set up the database connection
@pytest.fixture
def setup_db():
    repo = MysqlRepository()
    yield repo
    repo.connection.close()


def test_add_text(setup_db):
    # Create a Services instance with the setup repository
    service = Services(setup_db)

    # Add a text and retrieve its ID
    text_id = service.add_text("This is an example text", "example name", "example source", "en", "example genre")

    # Retrieve the text from the repository
    result = setup_db.get_text(text_id)

    # Assertions to check if the retrieved text matches the input
    assert result.text == "This is an example text"
    assert result.text_name == "example name"
    assert result.text_source == "example source"
    assert result.text_lang == "en"
    assert result.text_genre == "example genre"


def test_get_all_texts(setup_db):
    # Mock data to be returned by the repository
    expected_texts = [
        {'text': "This is an example text!", 'text_name': "example text", 'text_source': "test source",
         'text_lang': "en", 'text_genre': "test genre"}
    ]

    # Mock the repository method to return the mock data
    setup_db.get_all_texts = lambda: expected_texts

    # Create a Services instance with the setup repository
    service = Services(setup_db)

    # Retrieve all texts through the service
    texts = service.get_all_texts()

    # Assertions to check if the retrieved texts match the mock data
    assert len(texts) == 1
    assert texts[0].text == "This is an example text!"
    assert texts[0].text_name == "example text"
    assert texts[0].text_source == "test source"
    assert texts[0].text_lang == "en"
    assert texts[0].text_genre == "test genre"
