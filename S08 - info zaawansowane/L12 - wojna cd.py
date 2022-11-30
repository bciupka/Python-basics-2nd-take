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
battle = []

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
        player2.extend([card2, card1])
        print(
            "Player 2",
            card1["Power"],
            card2["Power"],
            len(player1),
            len(player2),
            sep="\t",
        )
    else:
        while len(player1) > 1 and len(player2) > 1:
            battle.extend([card1, card2])
            print(
                "Battle\t",
                card1["Power"],
                card2["Power"],
                sep="\t",
            )
            battle.append(player1.pop(0))
            battle.append(player2.pop(0))
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            if card1.get("Power") > card2.get("Power"):
                player1.extend(battle)
                player1.extend([card1, card2])
                print(
                    "\t",
                    card1["Power"],
                    card2["Power"],
                    len(player1),
                    len(player2),
                    sep="\t",
                )
                battle.clear()
                break
            elif card2.get("Power") > card1.get("Power"):
                player2.extend(battle)
                player2.extend([card1, card2])
                print(
                    "\t",
                    card1["Power"],
                    card2["Power"],
                    len(player1),
                    len(player2),
                    sep="\t",
                )
                battle.clear()
                break
            else:
                print(
                    "\t",
                    card1["Power"],
                    card2["Power"],
                    len(player1),
                    len(player2),
                    sep="\t",
                )
                continue
        else:
            if len(player1) <= 1:
                player1.clear()
            else:
                player2.clear()
            break
print("PLAYER 1 WINS!!!" if len(player2) < len(player1) else "PLAYER 2 WINS!!!")
