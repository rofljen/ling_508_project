from typing import List, Dict, Any
from Model.lexentry import LexEntry
from Model.text import Text
from db.mysql_repository import MysqlRepository
from db.repository import Repository
from Model.sentences import Sent

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

        # Optionally add words to the database
        self.add_words_from_text(text_id, text, text_lang)

        return text_id

    def get_text(self, text_id: int) -> Text:
        return self.repo.get_text(text_id)

    def get_all_texts(self):
        texts = self.repo.get_all_texts()
        # Map to the correct columns
        return [{'text_id': text['id'], 'text': text['text'], 'text_name': text['text_name'],
                 'text_source': text['text_source'], 'text_genre': text['text_genre'],
                 'text_lang': text['text_lang']} for text in texts]

    def split_into_sentences(self, text: str, text_lang: str) -> List[str]:
        sent_parser = Sent(text, text_lang)
        return sent_parser.sentences

    def add_words_from_text(self, text_id: int, text: str, lang: str) -> None:
        sentences = self.split_into_sentences(text, lang)

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

                # Insert words into the repository
                self.repo.insert_word(
                    text_id=text_id,
                    word_form=word,
                    pos=word_pos,
                    lemma=word_lemma,
                    gloss=gloss_str,
                    example=None
                )

    def analyze_text(self, text: str, lang: str) -> Dict[str, Any]:
        sentences = self.split_into_sentences(text, lang)
        analysis_results = []

        for sentence in sentences:
            lex_entry = LexEntry(form=sentence, pos=None, gloss=None, lang=lang)
            words = lex_entry.get_words()

            sentence_analysis = {
                'sentence': sentence,
                'words': []
            }

            for word in words:
                word_lex_entry = LexEntry(form=word, pos=None, gloss=None, lang=lang)
                word_pos = word_lex_entry.get_pos(word)
                word_lemma = word_lex_entry.lemmatize_word(word)
                glosses = word_lex_entry.get_gloss(word)

                gloss_str = '; '.join([f"{key}: {value['definition']} Example: {', '.join(value['examples'])}"
                                       for key, value in glosses.items()])

                sentence_analysis['words'].append({
                    'word_form': word,
                    'POS': word_pos,
                    'lemma': word_lemma,
                    'gloss': gloss_str
                })

            analysis_results.append(sentence_analysis)

        return {'analysis': analysis_results}
