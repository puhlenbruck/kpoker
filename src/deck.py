import random as rnd
from card import Card, Suite, Value

_card_list = [Card(suite=suite, value=value) for suite in Suite for value in Value]


class Deck:
    def __init__(self):
        self._deck = _card_list.copy()
        self.shuffle()

    def shuffle(self):
        rnd.shuffle(self._deck)

    def reset(self):
        self.__init__()

    def deal(self):
        return self._deck.pop()
