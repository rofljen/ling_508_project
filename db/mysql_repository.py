import mysql.connector
from mysql.connector import Error

class Repository:
    def __init__(Repository):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'ling_classifier'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

class TextRepository(Repository):
    def add_text(self, text, lang):
        query = "INSERT INTO texts (text, lang) VALUES (%s, %s)"
        return self.execute_query(query, (text, lang))

    def get_all_texts(self):
        query = "SELECT * FROM texts"
        return self.fetch_all(query)

class SentRepository(Repository):
    def add_sentence(self, text_id, sentence):
        query = "INSERT INTO sentences (text_id, sentence) VALUES (%s, %s)"
        return self.execute_query(query, (text_id, sentence))

    def get_sentences_by_text_id(self, text_id):
        query = "SELECT * FROM sentences WHERE text_id = %s"
        return self.fetch_all(query, (text_id,))