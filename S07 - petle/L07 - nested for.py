i = 10
x = 1
for j in range(1, i + 1):
    x *= j
print(x)

x = 1
for j in range(1, i + 1):
    x *= j
    print("{}\t{}".format(j, x))

list_noun = ["dog", "potato", "meal", "icecream", "car"]
list_adj = ["dirty", "big", "hot", "colorful", "fast"]

for j in list_noun:
    for k in list_adj:
        print(j, k)
