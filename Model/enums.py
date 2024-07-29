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
    NonFiction = "Non-Fiction"
    Fiction = "Fiction"
    News = "News"
    Science = "Science"

class Lang(Enum):
    en = "English"
    es = "Espanol"
    de = "Deutsch"
    fr = "Francais"
    it = "Italianio",
    nl = "Nederlands"
    pt = "Portuguese"
    xx = "Lang Neutral"