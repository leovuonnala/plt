
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"
        words = self.phrase.split()
        translated_words = []
        for word in words:
            if word[0] in 'aeiou':
                if word[-1] == 'y':
                    translated_word = word + 'nay'
                elif word[-1] in 'bcdfghjklmnpqrstvwxyz':
                    translated_word = word + 'ay'
                else:
                    translated_word = word + 'yay'
            else:
                translated_word = word + 'ay'
            translated_words.append(translated_word)
        return ' '.join(translated_words)

