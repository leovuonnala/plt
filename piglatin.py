
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
                else:
                    translated_word = word + 'yay'
            else:
                first_vowel_idx = next((i for i, letter in enumerate(word) if letter in 'aeiou'), None)
                if first_vowel_idx is not None:
                    translated_word = word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'
                else:
                    translated_word = word + 'ay'
            translated_words.append(translated_word)
        return ' '.join(translated_words)

