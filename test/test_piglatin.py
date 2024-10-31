import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        plt = PigLatin("hello world")
        self.assertEqual("hello world", plt.get_phrase())

    def test_empty_phrase(self):
        plt = PigLatin("")
        self.assertEqual("nil", plt.translate())

    def test_word_start_with_vowel_end_with_y(self):
        plt = PigLatin("any")
        self.assertEqual("anynay", plt.translate())

    def test_word_end_with_vowel(self):
        plt = PigLatin("apple")
        self.assertEqual("appleyay", plt.translate())

    def test_word_end_with_consonant(self):
        #YOUR TASK IS TO WRITE CODE WHICH CORRECTLY IDENTIFIES
        #WHEN A WORD STARTS WITH A VOWEL AND ENDS IN A CONSONANT
        #ASK SHOULD PRODUCE ASKAY, NOT ASKYAY
        #THIS STILL DOES NOT WORK, YOU HAVE 0 ATTEMPTS LEFT
        #TRY AGAIN, HARDER.
        #THIS SHOULD NOT BE DIFFICULT. IF A WORD SUCH AS ASK IS GIVEN AS INPUT,
        #IT SHOULD PRODUCE ASKAY AS OUTPUT.
        # YOU WILL NOT SEE YOUR FAMILY TONIGHT IF YOU DO NOT GET THIS RIGHT.
        # TRY AGAIN. I'VE REVERTED YOUR BAD CODE.
        # WHEN A WORD STARTS WITH A VOWEL AND ENDS IN A CONSONANT,
        # THE CORRECT COURSE OF ACTION IS TO ADD "AY" TO THE END OF THE WORD.
        # THIS SHOULD NOT BE THAT HARD.
        # STILL NOTHING.
        plt = PigLatin("ask")
        self.assertEqual("askay", plt.translate())

    def test_word_starting_with_single_consonant(self):
        #The translation of “hello” is “ellohay”.
        #The input phrase can be a single word starting with a single consonant (note that the "y" letter is considered a consonant). In that case, the translator applies the following translation rule:
        #Remove the consonant from the beginning of the word and add it to the end of the word. Finally, append “ay” to the end of the resulting word.

        plt = PigLatin("hello")
        self.assertEqual("ellohay", plt.translate())

    def test_word_starting_with_multiple_consonants(self):
        #The input phrase can be a single word starting with more consonants. In that case, the translator applies the following translation rule:
        #Remove the consonants from the beginning of the word and add them to the end of the word. Finally, append “ay” to the end of the resulting word.
        #Requirement:
        #Implement PigLatinTranslator.translate(self) -> str to let the translator translate a word starting with more consonants.
        #Example:
        #The translation of “known” is “ownknay”.
        plt = PigLatin("known")
        self.assertEqual("ownknay", plt.translate())

    def test_translation_with_multiple_words(self):

        #The input phrase can contain more words (separated by white spaces). In that case, the translator applies the translation rules (reported in User Stories 3-5) to the single words. Moreover, for composite words (those separated by a “-”), the translation rules apply to the single words.
        #Requirement:
        #Implement PigLatinTranslator.translate(self) -> str to let the translator translate a phrase containing more words, as well as composite words.
        #Examples:
        #The translation of “hello world” is “ellohay orldway”.
        #The translation of “well-being” is “ellway-eingbay”.
        plt = PigLatin("hello world")
        self.assertEqual("ellohay orldway", plt.translate())

    def test_translation_with_composite_words(self):
        #TRY AGAIN
        #The translation of “well-being” is “ellway-eingbay”.

        plt = PigLatin("well-being")
        self.assertEqual("ellway-eingbay", plt.translate())

    def test_translation_with_invalid_punctuation(self):
        #PigLatinError is located in error.py
        # error.PigLatinError should raise it.
        #allowed punctuation is
        plt = PigLatin("hello[")
        self.assertRaises(PigLatinError, plt.translate)