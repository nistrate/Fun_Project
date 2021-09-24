"""
In this notebook we will write the "War" card game dynamics

The game has two players and each player gets 26 cards
"""

if __name__ == "__main__":

    #first import all the classes we created

    import classes as cls

    # Let's create the game setup
    # players, deck, shuffle the deck, and distribute the deck to each player equally
    player_one = cls.Player("One")
    player_two = cls.Player("Two")

    new_deck = cls.Deck()
    new_deck.shuffle()

    for x in range( int(len(new_deck.all_cards)/2) ):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on = True    # Boolean value used to see if the game can continue or a winner must be declared
    round = 0         # Counter that keeps track of how many exchange rounds happened per game
    cards_at_war = 5  # Number of cards that are placed on the table at war round
    # Game dynamics

    while game_on:

        round += 1

        if len(player_one.all_cards) == 0:
            print(f"After {round} rounds:")
            print("Player One has zero cards left.\nPLayer Two wins the game!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print(f"After {round} rounds:")
            print("Player Two has zero cards left.\nPLayer One wins the game!")
            game_on = False
            break

        # cards on the table
        player_one_cards = []
        player_two_cards = []

        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())

        at_war = True  # let the game go on

        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False # end round

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False # end round

            else:
                if len(player_one.all_cards) < cards_at_war:
                    print(f"After {round} rounds:")
                    print("Player One doesn't have enough cards for War Round.\nPLayer Two wins the game!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < cards_at_war:
                    print(f"After {round} rounds:")
                    print("Player Two doesn't have enough cards for War Round.\nPLayer One wins the game!")
                    game_on = False
                    break

                else:
                    for i in range(cards_at_war):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

