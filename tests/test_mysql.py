import pytest
from mysql_repository import MysqlRepository

@pytest.fixture
def classifier_repo():
    return MysqlRepository()

def test_get_lang(classifier_repo):
    sql = "SELECT DISTINCT text_lang FROM text"
    classifier_repo.cursor.execute(sql)
    langs = classifier_repo.cursor.fetchall()
    assert len(langs) > 0

def test_pos(classifier_repo):
    sql = "SELECT pos from lex_entries"
    classifier_repo.cursor.execute(sql)
    pos_values = classifier_repo.cursor.fetchall()
    pos_set = set(value[0] for value in pos_values)
    expected_pos_tags = (
        "ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET",
        "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN",
        "PUNCT", "SCHEMES", "SCONJ", "SYM", "VERB", "X")
    assert pos_set.issubset(expected_pos_tags), f"Unexpected POS tags found: {pos_set - set(expected_pos_tags)}"

if __name__ == "__main__":
    pytest.main(["-v", __file__])
