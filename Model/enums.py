from enum import Enum
class PartofSpeech(Enum):
    ADJ = "ADJ"  # Adjective
    ADP = "ADP"  # Adposition
    ADV = "ADV"  # Adverb
    AUX = "AUX"  # Auxiliary verb
    CCONJ = "CCONJ"  # Coordinating conjunction
    DET = "DET"  # Determiner
    INTJ = "INTJ"  # Interjection
    NOUN = "NOUN"  # Noun
    NUM = "NUM"  # Numeral
    PART = "PART"  # Particle
    PRON = "PRON"  # Pronoun
    PROPN = "PROPN"  # Proper noun
    PUNCT = "PUNCT"  # Punctuation
    SCHEMES = "SCHEMES"  # Symbol
    SCONJ = "SCONJ"  # Subordinating conjunction
    SYM = "SYM"  # Symbol
    VERB = "VERB"  # Verb
    X = "X"

class Genre(Enum):
    NON_FICTION = "Non-Fiction"
    FICTION = "Fiction"
    NEWS = "News"
    SCIENCE = "Science"
    NONE = "None"

class Lang(Enum):
    nl = "nl_core_news_lg"
    en = "en_core_web_trf"
    fr = "fr_dep_news_trf"
    de = "de_dep_news_trf"
    it = "it_core_news_lg"
    xx = "xx_sent_ud_sm"
    pt = "pt_core_news_lg"
    es = "es_dep_news_trf"