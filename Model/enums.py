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
    en = 'en_core_web_sm'
    es = 'es_core_news_sm'
    de = 'de_core_news_sm'
    fr = 'fr_core_news_sm'
    it = 'it_core_news_sm'
    nl = 'nl_core_news_sm'
    pt = 'pt_core_news_sm'
    xx = 'xx_ent_wiki_sm'