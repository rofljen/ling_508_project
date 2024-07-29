import abc
from typing import List
from Model.text import Text


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_text(self) -> list[Text]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_text(self, text: Text) -> None:
        raise not NotImplementedError

    @abc.abstractmethod
    def get_text(self, text_id: int) -> Text:
        raise NotImplementedError
