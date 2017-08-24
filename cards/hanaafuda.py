################################################################################
## Hanafuda.py                                                                ##
##                                                                            ##
## Demo game for the card logic.                                              ##
##                                                                            ##
################################################################################

from card import Card
from deck import Deck
from hand import Hand


class HanafudaHand(Hand):
    def __init__(self, deck):
        self.create_hanafuda_deck()
        super.__init__(deck)

    def create_hanafuda_deck(self):
        card_template = Card()
        pass

    def match_pair(self, table):
        pass

    def draw_compare(self, draw, table):
        pass


