import random


colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
figures = [
    {"Figure": "Ace", "Power": 14},
    {"Figure": "King", "Power": 13},
    {"Figure": "Queen", "Power": 12},
    {"Figure": "Jack", "Power": 11},
    {"Figure": "10", "Power": 10},
    {"Figure": "9", "Power": 9},
]

allCards = []

for i in colors:
    for j in figures:
        aCard = j.copy()
        aCard.setdefault("Color", i)
        allCards.append(aCard)

random.shuffle(allCards)

player1 = allCards[:12]
player2 = allCards[12:]

print(player1)
print(player2)

while len(player1) != 0 and len(player2) != 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1.get("Power") > card2.get("Power"):
        player1.extend([card1, card2])
        print(
            "Player 1",
            card1["Power"],
            card2["Power"],
            len(player1),
            len(player2),
            sep="\t",
        )
    elif card1.get("Power") < card2.get("Power"):
        player2.extend([card1, card2])
        print(
            "Player 2",
            card1["Power"],
            card2["Power"],
            len(player1),
            len(player2),
            sep="\t",
        )
    else:
        player1.append(card1)
        player2.append(card2)
        print(
            "Equal\t",
            card1["Power"],
            card2["Power"],
            len(player1),
            len(player2),
            sep="\t",
        )
print("PLAYER 1 WINS!!!" if len(player2) == 0 else "PLAYER 2 WINS!!!")
