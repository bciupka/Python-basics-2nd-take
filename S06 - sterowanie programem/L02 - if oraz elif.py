minLikes = 500
minShares = 100

likesToday = 600
sharesToday = 20

if likesToday < minLikes:
    print('nie ma lajkow')
else:
    if sharesToday < minShares:
        print('nie ma shareow')
    else:
        print('PROMO')

if likesToday >= minLikes and sharesToday >= minShares:
    print('PROMO')
elif likesToday < minLikes:
    print('za malo likeow')
else:
    print('za malo shareow')
    
    
isPizza = False
isBigDrink = False
isWeekend = False

if isWeekend:
    print('weekend')
else:
    if not isBigDrink and not isPizza:
        print('zamowienie nie tak')
    else:
        print('PROMO')
    
if not isWeekend and (isBigDrink or isPizza):
    print('PROMO')
elif isWeekend:
    print('weekedzik')
else:
    print('domów')
    