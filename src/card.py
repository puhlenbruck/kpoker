from enum import Enum, unique
from functools import total_ordering


@unique
class Suite(Enum):
    SPADES = "spades"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"


@total_ordering
@unique
class Value(Enum):
    ACE = "Ace"
    KING = "King"
    QUEEN = "Queen"
    JACK = "Jack"
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2

    def __lt__(self, other):
        if not isinstance(other, Value):
            return NotImplemented
        if self == other:
            return False
        for value in Value:
            if value == self:
                return False
            if value == other:
                return True


class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.suite == other.suite and self.value == other.value

    def __repr__(self):
        return str(self.value.value) + " of " + str(self.suite.value)
