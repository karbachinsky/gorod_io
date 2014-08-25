"""
    Class allows morphology with words.
    Author: I. Karbachinsky
"""
import pymorphy2
from gorod.utils.decorators import Singleton


class WordProcessor(Singleton):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()

    def inflect(self, word, form):
        """
            Inflect word to certain form
            Available forms: ..., gent, ...
        """
        wordmorph = self.morph.parse(word)
        return wordmorph[0].inflect({form})[0]
