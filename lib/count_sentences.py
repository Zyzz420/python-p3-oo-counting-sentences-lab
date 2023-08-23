class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise TypeError("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if self.is_sentence() or self.is_question() or self.is_exclamation():
            sentences = [sentence.strip() for sentence in self._value.split(".") if sentence.strip()]
            return len(sentences)
        else:
            return 0