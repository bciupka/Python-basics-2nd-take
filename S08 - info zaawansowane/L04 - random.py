import random

for i in range(10):
    print(random.randint(1, 100))  # 1 <= x <= 100 - range dla randinta zamknięty

number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
tries = 1
while number1 != number2:
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    tries += 1
print(number1, number2, tries)

countries = [
    "Uruguay",
    "Russia",
    "Saudi Arabia",
    "Egypt",
    "Spain",
    "Portugal",
    "Iran",
    "Morocco",
    "France",
    "Denmark",
    "Peru",
    "Australia",
    "Croatia",
    "Argentina",
    "Nigeria",
    "Iceland",
    "Brazil",
    "Switzerland",
    "Serbia",
    "Costa Rica",
    "Sweden",
    "Mexico",
    "Korea Republic",
    "Germany",
    "Belgium",
    "England",
    "Tunisia",
    "Panama",
    "Colombia",
    "Japan",
    "Senegal",
    "Poland",
]

random.shuffle(countries)

group = 0

i = 0
while i<len(countries):
    if i % 4 == 0:
        group += 1
        print("Group {}\n{}".format(group, countries[i]))
    else:
        print(countries[i])
    i += 1