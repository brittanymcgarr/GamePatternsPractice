################################################################################
## Card.py                                                                    ##
##                                                                            ##
## Card level logic for the game.                                             ##
##                                                                            ##
################################################################################

from random import randint


class Card:
    suits = set()
    ranks = set()

    def __init__(self, name=None, suit=None, rank=None:
        self.name = name
        self.suit = suit
        self.rank = rank
        self.suits.add(suit)
        self.ranks.add(rank)

    def randomize(self):
        if self.suits:
            position = randint(0, len(self.suits) - 1)
            self.suit = list(self.suits)[position]

        if self.ranks:
            position = randint(0, len(self.suits) - 1)
            self.rank = list(self.ranks)[position]

