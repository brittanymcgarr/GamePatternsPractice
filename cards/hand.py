################################################################################
## Hand.py                                                                    ##
##                                                                            ##
## Hand level logic for the game. Inherit to specific rules.                  ##
##                                                                            ##
################################################################################

from card import Card
from deck import Deck


class Hand:
    def __init__(self, deck):
        if isinstance(deck, Deck):
            pass

