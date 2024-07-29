CREATE DATABASE ling_classifier;
ALTER DATABASE ling_classifier CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE ling_classifier;

CREATE TABLE text (
    id INT NOT NULL AUTO_INCREMENT,
    text LONGTEXT,
    text_name NVARCHAR(255),
    text_source VARCHAR(255),
    text_lang NVARCHAR(255),
    text_genre NVARCHAR(50),
    word_count INT,
    PRIMARY KEY (id)
);

CREATE TABLE lex_entries (
    id INT NOT NULL AUTO_INCREMENT,
    text_id INT NOT NULL,
    word_form NVARCHAR(50),
    pos NVARCHAR(50),
    lemma NVARCHAR(50),
    gloss TEXT,
    example TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (text_id) REFERENCES text(id)
);

CREATE TABLE glosses (
    id INT NOT NULL AUTO_INCREMENT,
    lex_entry_id INT NOT NULL,
    word_form NVARCHAR(50),
    gloss TEXT,
    example TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (lex_entry_id) REFERENCES lex_entries(id)
);

INSERT INTO text (text, text_name, text_source, text_lang, text_genre, word_count)
VALUES(
    'Every year we go to Florida. We like to go to the beach. My favorite beach is called Emerson Beach.
    It is very long, with soft sand and palm trees. It is very beautiful. I like to make sandcastles and watch the sailboats go by.
    Sometimes there are dolphins and whales in the water! Eve'ry morning we look for shells in the sand.
    I found fifteen big shells last year. I put them in a special place in my room.
    This year I want to learn to surf. It is hard to surf, but so much fun! My sister is a good surfer.
    She says that she can teach me. I hope I can do it!', 
    'Our Vacation', 
    'https://lingua.com/english/reading/vacation/', 
    'English', 
    'Non-Fiction', 
    118
);
