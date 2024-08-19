import abc
from typing import List
from Model.text import Text


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_text(self) -> List[Text]:
        """
        Load all texts from the repository.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_text(self, text: Text) -> None:
        """
        Add a new text to the repository.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_text(self, text_id: int) -> Text:
        """
        Retrieve a text by its ID.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def insert_text(self, text: str, text_name: str, text_source: str, text_lang: str, text_genre: str,
                    word_count: int) -> int:
        """
        Insert a new text into the repository and return its ID.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def insert_word(self, text_id: int, word_form: str, pos: str, lemma: str, gloss: str, example: str) -> None:
        """
        Insert a word entry into the repository.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_texts(self) -> List[Text]:
        """
        Retrieve all texts from the repository.
        """
        raise NotImplementedError
