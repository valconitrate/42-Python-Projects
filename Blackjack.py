import random
import random as rd
from random import randint as ri

p1 = {"cards": [], "sum": 0}
p2 = {"cards": [], "sum": 0}

diamond = {"A" : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "J" : 10, "Q" : 10, "K" : 10}
heart = {"A" : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "J" : 10, "Q" : 10, "K" : 10}
club = {"A" : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "J" : 10, "Q" : 10, "K" : 10}
spade = {"A" : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "J" : 10, "Q" : 10, "K" : 10}
deck = {"diamond": diamond, "heart": heart, "club": club, "spade": spade}

def getCard():
    # Returns a suit type and a card number
    suit = random.choice(list(deck.keys()))
    # print(suit, type(suit))
    card = random.choice((list(deck[suit].items())))
    # print(card, type(card))
    ccard = [card, suit]
    return ccard

face = ["J", "Q", "K"]

# assign p1 cards
p1["cards"].append(getCard())
p1["cards"].append(getCard())
total = 0
if (p1["cards"][0][0][0] in face and p1["cards"][1][0][0] == "A") or (p1["cards"][0][0][0] == "A" and p1["cards"][1][0][0] in face):
    total = 21
else:
    for i in p1["cards"]:
        total += i[0][1]
p1["sum"] = total

# assign p2 cards
p2["cards"].append(getCard())
p2["cards"].append(getCard())
total = 0
if (p2["cards"][0][0][0] in face and p2["cards"][1][0][0] == "A") or (p2["cards"][0][0][0] == "A" and p2["cards"][1][0][0] in face):
    total = 21
else:
    for i in p2["cards"]:
        total += i[0][1]
p2["sum"] = total

# Notation:
# pn["cards"][card 1 or card 2][card number or suit][if card number: notation or value]

print("Dealer's card is: ", p1["cards"][0][0][0], p1["cards"][0][1])
print("Your cards are: ", p2["cards"][0][0][0], p2["cards"][0][1], " and ", p2["cards"][1][0][0], p2["cards"][1][1])

