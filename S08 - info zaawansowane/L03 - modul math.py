import math

deg = 360
print(deg / 180 * math.pi, math.radians(deg))

deg = 45
print(deg / 180 * math.pi, math.radians(deg))

smallR = 22
bigR = 27
famR = 38
smallP = 11.5
bigP = 15.6
famP = 22

samllA = smallR**2 * math.pi / 10000
bigA = bigR**2 * math.pi / 10000
famA = famR**2 * math.pi / 10000

smallM = smallP / samllA
bigM = bigP / bigA
famM = famP / famA
print(smallM, bigM, famM)
