import mysql.connector
from mysql.connector import Error
from Model.enums import PartofSpeech
from Model.lexentry import LexEntry

class MysqlRepository:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'ling_classifier'
        }
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def __del__(self):
        self.close()

    def map_pos(self, pos_str: str) -> PartofSpeech:
        pos_switcher = {
            'VERB': PartofSpeech.VERB,
            'NOUN': PartofSpeech.NOUN,
            'ADJ': PartofSpeech.ADJECTIVE,
            'ADV': PartofSpeech.ADVERB,
            'PRON': PartofSpeech.PRONOUN,
            'DET': PartofSpeech.DETERMINER,
            'ADP': PartofSpeech.PREPOSITION
        }
        return pos_switcher.get(pos_str, None)

    def mapper(self, entry: dict) -> LexEntry:
        return LexEntry(
            form=entry.get('form'),
            pos=self.map_pos(entry.get('pos')),
            gloss=entry.get('definition')
        )

    def load_lexicon(self) -> list[LexEntry]:
        try:
            sql = 'SELECT * FROM lex_entries'
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            entries = [{'id': id, 'form': form, 'lemma': lemma, 'pos': pos, 'gloss': gloss, 'ex': ex}
                       for (id, form, lemma, pos, gloss, ex) in results]
            lex_entries = [self.mapper(entry) for entry in entries]
            return lex_entries
        except Error as e:
            print(f"Error loading lexicon: {e}")
            return []
