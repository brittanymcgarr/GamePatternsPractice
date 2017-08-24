################################################################################
## Deck.py                                                                    ##
##                                                                            ##
## Deck level logic and initialization for the game.                          ##
##                                                                            ##
################################################################################

from card import Card


class Deck:
    card_template = None

    def __init__(self, card_template, size):
        if isinstance(card_template, Card) and isinstance(size, int):
            self.card_template = card_template
            self.size = size

            self.initialize_deck()

    def initialize_deck(self):
        pass