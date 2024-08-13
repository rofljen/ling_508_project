-- Create the database and set charset
CREATE DATABASE IF NOT EXISTS ling_classifier;
ALTER DATABASE ling_classifier CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE ling_classifier;

-- Create the `text` table
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

-- Create the `lex_entries` table
CREATE TABLE IF NOT EXISTS lex_entries (
    id INT NOT NULL AUTO_INCREMENT,
    text_id INT NOT NULL,
    word_form VARCHAR(50),
    pos VARCHAR(50),
    lemma VARCHAR(50),
    gloss TEXT,
    example TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (text_id) REFERENCES text(id) ON DELETE CASCADE
);

-- Create the `glosses` table
CREATE TABLE IF NOT EXISTS glosses (
    id INT NOT NULL AUTO_INCREMENT,
    lex_entry_id INT NOT NULL,
    word_form VARCHAR(50),
    gloss TEXT,
    example TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (lex_entry_id) REFERENCES lex_entries(id) ON DELETE CASCADE
);

-- Insert initial data into the `text` table
INSERT IGNORE INTO text (text, text_name, text_source, text_lang, text_genre, word_count)
VALUES ('this is my example text', 'example text', 'example source', 'en', 'example genre', 5);
