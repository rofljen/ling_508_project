-- Check if database exists before creating it
CREATE DATABASE IF NOT EXISTS ling_classifier;
ALTER DATABASE ling_classifier CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE ling_classifier;

-- Check if table exists before creating it
CREATE TABLE IF NOT EXISTS text (
    id INT NOT NULL AUTO_INCREMENT,
    text LONGTEXT,
    text_name VARCHAR(255),
    text_source VARCHAR(255),
    text_lang VARCHAR(255),
    text_genre VARCHAR(50),
    word_count INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS lex_entries (
    id INT NOT NULL AUTO_INCREMENT,
    text_id INT NOT NULL,
    word_form VARCHAR(50),
    pos VARCHAR(50),
    lemma VARCHAR(50),
    gloss TEXT,
    example TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (text_id) REFERENCES text(id)
);

CREATE TABLE IF NOT EXISTS glosses (
    id INT NOT NULL AUTO_INCREMENT,
    lex_entry_id INT NOT NULL,
    word_form VARCHAR(50),
    gloss TEXT,
    example TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (lex_entry_id) REFERENCES lex_entries(id)
);

-- Insert data if it does not already exist
INSERT IGNORE INTO text (text, text_name, text_source, text_lang, text_genre, word_count)
VALUES(
    'Every year we go to Florida. We like to go to the beach. My favorite beach is called Emerson Beach. It is very long, with soft sand and palm trees. It is very beautiful. I like to make sandcastles and watch the sailboats go by. Sometimes there are dolphins and whales in the water! Every morning we look for shells in the sand. I found fifteen big shells last year. I put them in a special place in my room. This year I want to learn to surf. It is hard to surf, but so much fun! My sis
