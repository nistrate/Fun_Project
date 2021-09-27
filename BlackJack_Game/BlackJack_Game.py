"""
This script is used to create the game dynamic
for the Black Jack Game.

Author: Nicolae Istrate
"""

import classes

# Create elements in the game

my_deck = classes.Deck()
my_deck.shuffle()

stay = False
dealer_won = False

player_cards = []
dealer_cards = []

player = classes.Player("Jack")
dealer = classes.Player("Dealer")

player_cards.append(my_deck.deal_one())
dealer_cards.append(my_deck.deal_one())
player_cards.append(my_deck.deal_one())
dealer_special_card = my_deck.deal_one()

player_hand_value = classes.hand_value(player_cards)
dealer_hand_value = classes.hand_value(dealer_cards)

print(f'{player.name}`s hand value is {player_hand_value}')
print(f'{dealer.name}`s hand value is {dealer_hand_value}')

# Player's turn

while not stay:
    if player_hand_value > 21:
        print(f'{player.name} has lost the GAME')
        stay = True
        dealer_won = True
        break

    turn_value = input("Type 'Hit' for new card or 'Stay' to end your turn:")

    if turn_value == 'Stay':
        print('Your turn has ended\n\t'f'{player.name}`s hand value is {player_hand_value}')
        print(f'\t{dealer.name}`s hand value is {dealer_hand_value}')
        stay = True
        break
    if turn_value == 'Hit':
        player_cards.append(my_deck.deal_one())
        player_hand_value = classes.hand_value(player_cards)
        print(f'\t{player.name}`s hand value is {player_hand_value}')

# Dealer's turn
if dealer_won == False:
    print('Dealer`s Turn')
    dealer_threshold =  21 - 11

    while dealer_hand_value < dealer_threshold:
        dealer_cards.append(my_deck.deal_one())
        dealer_hand_value = classes.hand_value(dealer_cards)
        print(f'Dealer adds card: hand value = {dealer_hand_value}')

    # End Game dynamics
    dealer_hand_value += dealer_special_card.value
    print(f'Dealer hand value = {dealer_hand_value}')
    player_diff = 21 - player_hand_value

    dealer_diff = 21 - dealer_hand_value
    if dealer_hand_value > 21:
        print(f'{player.name} has WON the GAME')
    elif dealer_diff > player_diff:
        print(f'{player.name} has WON the GAME')
    elif dealer_diff < player_diff:
        print(f'{dealer.name} has Won the GAME')
    else:
        print('The GAME is TIED')


