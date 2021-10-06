import random

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


def assignSum(card):
    face = ["J", "Q", "K"]
    total = 0
    if (card["cards"][0][0][0] in face and card["cards"][1][0][0] == "A") or (
            card["cards"][0][0][0] == "A" and card["cards"][1][0][0] in face):
        total = 21
    else:
        for i in card["cards"]:
            total += i[0][1]
    card["sum"] = total


def showCards(player):
    for i in player["cards"]:
        print(i[0][0], i[1], end=" ")
    print("Total: ", player["sum"])

# game start
game_state = True

while game_state:
    p1 = {"cards": [], "sum": 0}
    p2 = {"cards": [], "sum": 0}

    # assign p1 cards
    p1["cards"].append(getCard())
    p1["cards"].append(getCard())
    assignSum(p1)

    # assign p2 cards
    p2["cards"].append(getCard())
    p2["cards"].append(getCard())
    assignSum(p2)

    print("Dealer's card is: ", p1["cards"][0][0][0], p1["cards"][0][1])
    print("Your cards are: ", p2["cards"][0][0][0], p2["cards"][0][1], " and ", p2["cards"][1][0][0], p2["cards"][1][1])

    another = input("Would you like to (1)Call or (2)Draw another card ? ")

    if int(another) == 2:
        p2["cards"].append(getCard())
        assignSum(p2)

    showCards(p1)
    showCards(p2)

    if p2["sum"] < p1["sum"] or p2["sum"]>21:
        print("You lose")
    elif p2["sum"] > p1["sum"]:
        print("You win")
    elif p2["sum"] == p1["sum"]:
        print("Draw")
    else:
        print("Compute Error")

    again = input("Would you like to try again? (y/n): ")
    if again == "y":
        pass
    elif again == "n":
        game_state = False
    else:
        print("invalid input")