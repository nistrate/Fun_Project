'''
In this notebook we will create all the classes necessary for the dynamics of the War Card Game.
The classes displayed here are:
    1) Card Class - a class that creates card objects with attributes:
        suit and rank
    2) Deck Class

    3) Player Class
'''

# First though, we will create a

# 1) dictionary that relates rank with value ( ex: 'Seven' = 7, 'Queen' = 12)

values = {'Two' : 2 , 'Three' : 3 , 'Four'  : 4 , 'Five' : 5,
          'Six' : 6 , 'Seven' : 7 , 'Eight' : 8 , 'Nine' : 9,
          'Ten' : 10, 'Jack'  : 11, 'Queen' : 12, 'King' : 13, 'Ace' : 14}

# 2) tuple list that stores the possible suits of the playing cards

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# 3) tuple list that stores the possible ranks of the playing cards

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')

# Now let's create the classes used in the dynamics of teh game

class Card():
    """
    class that creates card objects with attributes:
    suit, rank, and value

    also we added a special method used to print info of the created object
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank] # uses the provided rank to determine the value of the card

    def __str__(self):
        return self.rank + " of " + self.suit


from random import shuffle

class Deck():
    """
    class used to create a full deck of playing cards (52)

    methods:
        1) shuffle - shuffles the deck of cards using random.shuffle()
        2) deal_one - deals one card from the top (position -1)
    """

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():
    """
    player class that deals with the cards + game actions the player performs

    attributes:
        1) name - name of each player

    methods:
        1) remove_one - removes a card from the player's card
        2) add_cards  - takes the won cards and places at the bottom of the players card (position 0)
        3) __str__    - prints the number of cards that each player has
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):  # if multiple cards to add
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

if __name__ == "__main__":
    my_card = Card("Hearts", "Queen")
    print(f'My card: {my_card} with Value {my_card.value}.')