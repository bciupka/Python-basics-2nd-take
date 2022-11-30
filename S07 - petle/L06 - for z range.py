string_A = "+---+---+---+---+"
string_B = "|   |   |   |   |"

for i in range(10):
    print(string_A)

print("\n\n")

for i in range(9):
    print(string_A if i % 2 == 0 else string_B)

for i in range(9):
    print((i + 1) * "x")


for i in range(9):
    print((i + 1) * "o" if i % 2 == 0 else (i + 1) * "x")
