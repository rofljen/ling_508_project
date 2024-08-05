from typing import List
from Model.text import Text
from Model.lexentry import LexEntry
from db.mysql_repository import MysqlRepository
from db.repository import Repository

class Services:
    def __init__(self, repository: Repository = None):
        self.repo = repository or MysqlRepository()  # Default to MysqlRepository if no instance provided

    def add_text(self, content: str, text_name: str, text_source: str, text_lang: str, text_genre: str) -> int:
        text = Text(text=content, text_name=text_name, text_source=text_source, text_lang=text_lang,
                    text_genre=text_genre, word_count=len(content.split()))
        text_id = self.repo.insert_text(content, text_name, text_source, text_lang, text_genre, text.word_count)
        self.add_words_from_text(text_id, content, text_lang)
        return text_id

    def add_words_from_text(self, text_id: int, content: str, lang: str) -> None:
        text = Text(text=content, text_lang=lang)
        sentences = text.split_into_sent()
        for sentence in sentences:
            lex_entry = LexEntry(sentence, lang=lang)
            for word in lex_entry.return_lex_entries():
                pos = lex_entry.get_pos(word)
                lemma = lex_entry.lemmatize_word(word)
                glosses = lex_entry.get_sense(word)
                for gloss, details in glosses.items():
                    for example in details['examples']:
                        self.repo.insert_word(text_id, word, pos, lemma, gloss, example)

    def get_all_texts(self) -> List[Text]:
        texts_data = self.repo.get_all_texts()
        texts = [Text(**data) for data in texts_data]
        return texts
