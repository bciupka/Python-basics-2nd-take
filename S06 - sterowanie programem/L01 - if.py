minLikes = 500
minShares = 100

likesToday = 600
sharesToday = 20

if likesToday >= minLikes and sharesToday >= minShares:
    print("PROMO!!!")
else:
    print("NO PROMO :(")

isPizza = False
isBigDrink = True
isWeekend = True

if not isWeekend and (isPizza or isBigDrink):
    print("BURGER!!!")
else:
    print("NO BURGER :(")

diskSize = 140
diskSizeUsed = 133
fileSize = 7

if diskSize - diskSizeUsed >= fileSize:
    print("OK")
else:
    print("NOK")
