class Sent:
    def __init__(self, sentences):
        self.sentences = [sentence for sentence in sentences]

    def get_sentence(self, index):
        if index < 0 or index >= len(self.sentences):
            raise IndexError("Index out of range")
        return self.sentences[index]

    def __str__(self):
        return ' '.join(self.sentences)