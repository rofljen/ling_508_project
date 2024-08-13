import mysql.connector
from mysql.connector import Error
from Model.lexentry import LexEntry
from Model.text import Text

class MysqlRepository:
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',  # Use 'localhost' if running locally
            'port': '3306',
            'database': 'ling_classifier'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if  self.connection:
            self.connection.close()

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def map_pos(self, pos: str) -> str:
        # Example POS mapping function
        pos_mapping = {'NOUN': 'Noun', 'VERB': 'Verb'}
        return pos_mapping.get(pos, 'Unknown')

    def mapper(self, entry: dict) -> LexEntry:
        form = entry.get('form', '')
        pos = self.map_pos(entry.get('pos', ''))
        gloss = entry.get('gloss', '')
        lemma = entry.get('lemma', None)
        example = entry.get('example', None)
        sentence = None  # Set this as needed or remove if not used

        return LexEntry(form=form, pos=pos, gloss=gloss, lemma=lemma, example=example, sentence=sentence)

    def load_lexicon(self) -> list[LexEntry]:
        try:
            sql = 'SELECT * FROM lex_entries'  # Ensure table name matches
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            entries = [{'id': id, 'form': form, 'lemma': lemma, 'pos': pos, 'gloss': gloss, 'ex': ex}
                       for (id, form, lemma, pos, gloss, ex) in results]
            lex_entries = [self.mapper(entry) for entry in entries]
            return lex_entries
        except Error as e:
            print(f"Error loading lexicon: {e}")
            return []

    def insert_text(self, text, text_name, text_source, text_lang, text_genre, word_count):
        query = """INSERT INTO text (text, text_name, text_source, text_lang, text_genre, word_count) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        try:
            self.cursor.execute(query, (text, text_name, text_source, text_lang, text_genre, word_count))
            self.connection.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(f"Error inserting text: {e}")
            self.connection.rollback()

    def insert_word(self, text_id, word_form, pos, lemma, gloss, example):
        query = """INSERT INTO lex_entry (text_id, word_form, pos, lemma, gloss, example) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        try:
            self.cursor.execute(query, (text_id, word_form, pos, lemma, gloss, example))
            self.connection.commit()
        except Error as e:
            print(f"Error inserting word: {e}")
            self.connection.rollback()

    def get_all_texts(self):
        query = "SELECT * FROM text"  # Ensure table name matches
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching texts: {e}")
            return []

    def get_text_by_id(self, text_id):
        query = "SELECT * FROM text WHERE id = %s"
        self.cursor.execute(query, (text_id,))  # Notice the tuple here
        result = self.cursor.fetchone()
        if result:
            return {
                'id': result[0],
                'text': result[1],
                'text_name': result[2],
                'text_source': result[3],
                'text_lang': result[4],
                'text_genre': result[5],
                'word_count': result[6]
            }
        return None