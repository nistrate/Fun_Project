"""
This script is used to create all the classes
and store tuples/ constants/ dictionaries/ global variables
for the Black Jack Game.

Author: Nicolae Istrate
"""

# For start we will create lists of tuples that will store the
# possible suit and rank of playing cards

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
         "Jack", "Queen", "King", "Ace")

# Next we create a dictionary that stores the numerical value associated with each rank

# Note: For now we will treat the Ace as being values at 1, however
# in the next iteration of the script, we will make it worth 1 or 10 (depending on the context of the game)

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6,
          "Seven":7, "Eight":8, "Nine":9, "Ten":10,
         "Jack":10, "Queen":10, "King":10, "Ace":1}

# Now, let's implement some classes.

# The Card class

class Card():
    """
    class that creates card objects
    Attributes:
        suit, rank, and value
    Methods
        __str__
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit} worth {self.value}."

from random import shuffle  # used in shuffling the deck

class Deck():
    """
    class that creates a Deck of cards
    Attributes:
        all_cards
    Methods:
        deal_one
        shuffle
    """

    def __init__(self):
        self.all_cards = []

        for rank in ranks:
            for suit in suits:
                self.all_cards.append(Card(rank, suit))

    def deal_one(self):
        return self.all_cards.pop()

    def shuffle(self):
        shuffle(self.all_cards)


class Player():
    """
    class that creates a Player
    Attributes:
        name, player_cards
    Methods:
        hit (add_new_card)
        hand_value (calculates the value of all cards in the hand)
    """

    def __init__(self, name):
        self.name = name
    #     self.player_cards = []
    #
    # def hit(self, new_card):
    #     self.player_cards.append(new_card)
    #
    # def hand_value(self):
    #     self.value = 0
    #     for card in player_cards:
    #         self.value += card.value

class Dealer():
    """
    class that creates a Dealer
    Attributes:
        name = Dealer, dealer_cards
    Methods:
        hit (add_new_card)
        special_card (hit but face down)
        hand_value (calculates the value of all cards in the hand)

    """

    def __init__(self, name= 'Dealer'):
        self.name = name
    #     self.dealer_cards = []
    #
    # def hit(self, new_card):
    #     self.dealer_cards.append(new_card)
    #
    # def special_card(self, new_card):
    #     return new_card
    #
    # def hand_value(self):
    #     self.value = 0
    #     for card in dealer_cards:
    #         self.value += card.value


def hand_value(your_card_list):
    value = 0
    for card in your_card_list:
        value += card.value
    return value
