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
    word_form NVARCHAR(255),
    pos NVARCHAR(50),
    lemma NVARCHAR(255),
    gloss TEXT,
    example TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (text_id) REFERENCES text(id)
);