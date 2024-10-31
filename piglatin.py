
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
            if '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_subword(subword) for subword in subwords]
                translated_word = '-'.join(translated_subwords)
            else:
                translated_word = self.translate_subword(word)
            translated_words.append(translated_word)
        return ' '.join(translated_words)

    def translate_subword(self, word):
        if word[0] in 'aeiou':
            if word[-1] == 'y':
                return word + 'nay'
            elif word[-1] in 'bcdfghjklmnpqrstvwxyz':
                return word + 'ay'
            else:
                return word + 'yay'
        else:
            consonant_cluster = ''
            rest_of_word = word
            for char in word:
                if char in 'bcdfghjklmnpqrstvwxyz':
                    consonant_cluster += char
                    rest_of_word = rest_of_word[1:]
                else:
                    break
            return rest_of_word + consonant_cluster + 'ay'

