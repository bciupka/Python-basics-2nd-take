import random


colors = ["Hearts", "Diamonds", "Clubs", "Spades"]

figures = ["Ace", "King", "Queen", "Jack", "10", "9"]

allCards = []

for i in colors:
    for j in figures:
        allCards.append("{} of {}".format(j, i))

random.shuffle(allCards)

print(allCards)

player1 = []
player2 = []

for i in allCards:
    if allCards.index(i) % 2 == 0:
        player1.append(i)
    else:
        player2.append(i)

print(player1)
print(player2)

player3 = allCards[:12]
player4 = allCards[12:]

print(player3)
print(player4)
