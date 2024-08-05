from app.services import Services

if __name__ == "__main__":
    services = Services()
    lang = input("Please enter the language code")
    text_input = Text(lang=lang)
    text_input = Text()
    text_input.accept_input()
    sentences = text_input.split_into_sent()
    print("Sentences:", sentences)

    sent = Sent(sentences)

    for i, sentence in enumerate(sentences):
        print(f"\nAnalyzing Sentence {i}: {sentence}")
        lex_entry = LexEntry(sentence)
        print("Words in the sentence:", lex_entry.split_into_words())
        print("Word lengths:", lex_entry.get_word_len())
        for word in lex_entry.split_into_words():
            print(f"Word: {word}")
            print(f"Index of the word: {lex_entry.get_word_index(word)}")
            print(f"POS of the word: {lex_entry.get_pos(word)}")
            print(f"Lemmatized form of the word: {lex_entry.lemmatize_word(word)}")
            print(f"Sense of the word: {lex_entry.get_sense(word)}")