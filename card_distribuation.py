import random

# Define the cardType and ranks of the cards

cardTypes = ['H', 'D', 'B', 'ita']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jocker', 'Queen', 'King', 'A']

# Create a deck of cards
deck = [f'{rank} of {Type}' for Type in cardTypes for rank in ranks]
print(deck)
# Shuffle the deck
random.shuffle(deck)
# print(random.choice(deck))

# Distribute cards to four players
players = {f'Player {i+1}': [] for i in range(4)}

for i in range(52):
    player_number = i % 4  # Determine which player gets the card
    players[f'Player {player_number + 1}'].append(deck[i])

# Display the cards for each player
for player, cards in players.items():
     print(f'{player} has the following cards:')
    #  print(', '.join(cards))
     print(cards) #Print cards with cardtype
     print()  # Print a newline for better readability


# for()