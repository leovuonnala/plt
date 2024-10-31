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