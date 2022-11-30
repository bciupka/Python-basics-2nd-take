firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print("Row number", currentRow)
    currentRow += 1


i = 1
while i <= 13:
    print(i**2, i**3, sep="\t")
    i += 1

i = 0
while i <= 16:
    print(2**i)
    i += 1

print(5 * "x")

i = 1
while i <= 10:
    print(i * "x")
    i += 1
