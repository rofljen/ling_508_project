import pytest
from app.services import Services
from db.mysql_repository import MysqlRepository

@pytest.fixture
def service():
    repo = MysqlRepository()
    return Services(repo)

def test_service_add_text(service):
    text_data = {
        'text': "Sample text",
        'text_name': "Sample Name",
        'text_source': "Sample Source",
        'text_lang': "en",
        'text_genre': "Sample Genre"
    }

    # Call the add_text method to insert data
    text_id = service.add_text(
        text_data['text'],
        text_data['text_name'],
        text_data['text_source'],
        text_data['text_lang'],
        text_data['text_genre']
    )

    # Retrieve the data from the database
    result = service.repo.get_text_by_id(text_id)

    # Verify the text was added correctly
    assert result is not None
    assert result['text'] == text_data['text']
    assert result['text_name'] == text_data['text_name']
    assert result['text_source'] == text_data['text_source']
    assert result['text_lang'] == text_data['text_lang']
    assert result['text_genre'] == text_data['text_genre']

    # Optionally, clean up data if needed
    # service.repo.delete_text_by_id(text_id)  # Implement if needed
