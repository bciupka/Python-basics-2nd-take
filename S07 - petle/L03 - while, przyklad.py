import random


i = 0

while i + 1 <= 50:
    print(i * 2 + 1)
    i += 1

my_number = random.randint(0, 10)
guess = -1
trials = 0
while guess != my_number:
    guess = int(input())
    trials += 1
    print("try again" if guess != my_number else "nice")
print("trials=", trials)
