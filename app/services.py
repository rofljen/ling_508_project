from typing import List
from Model.text import Text
from Model.lexentry import LexEntry
from db.mysql_repository import MysqlRepository
from db.repository import Repository


def split_into_sentences(text, text_lang) -> List[str]:
    text_obj = Text(text=text, text_lang=text_lang)
    sentences = text_obj.split_into_sent()
    return sentences


class Services:
    def __init__(self, repository: Repository = None):
        self.repo = repository or MysqlRepository()

    def add_text(self, text: str, text_name: str, text_source: str, text_lang: str, text_genre: str) -> int:
        word_count = len(text.split())
        text_obj = Text(text=text, text_name=text_name, text_source=text_source, text_lang=text_lang,
                        text_genre=text_genre, word_count=word_count)

        text_id = self.repo.insert_text(
            text=text,
            text_name=text_name,
            text_source=text_source,
            text_lang=text_lang,
            text_genre=text_genre,
            word_count=word_count
        )

        self.add_words_from_text(text_id, text, text_lang)

        return text_id

    def get_text(self, text_id: int) -> Text:
        return self.repo.get_text(text_id)

    def get_all_texts(self) -> List[Text]:
        return self.repo.get_all_texts()

    def add_words_from_text(self, text_id: int, text: str, lang: str):
        sentences = split_into_sentences(text, lang)

        for sentence in sentences:
            lex_entry = LexEntry(form=sentence, pos=None, gloss=None, lang=lang)
            words = lex_entry.get_words()

            for word in words:
                word_lex_entry = LexEntry(form=word, pos=None, gloss=None, lang=lang)
                word_pos = word_lex_entry.get_pos(word)
                word_lemma = word_lex_entry.lemmatize_word(word)
                glosses = word_lex_entry.get_gloss(word)

                gloss_str = '; '.join([f"{key}: {value['definition']} Example: {', '.join(value['examples'])}"
                                       for key, value in glosses.items()])

                self.repo.insert_word(
                    text_id=text_id,
                    word_form=word,
                    pos=word_pos,
                    lemma=word_lemma,
                    gloss=gloss_str,
                    example=None
                )

