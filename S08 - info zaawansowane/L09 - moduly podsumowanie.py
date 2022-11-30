inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
factortable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]

import datetime
import math
import random

if len(inputdata) == len(factortable):
    print("OK")
    i = 0
    while i < len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        minint = math.floor(minvalue)
        maxint = math.ceil(maxvalue)
        print(minint, inputdata[i], maxint)
        i += 1

else:
    print("inputdata and factortable need to have equal number of elements")


i = 0
while i < len(inputdata):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = (
        inputdata[i] + random.uniform(0, 1.0) * inputdata[i]
    )  # uniform przedział zamknięty dwustronnie, random zamknięty tylko od zera
    minint = math.floor(minvalue)
    maxint = math.ceil(maxvalue)
    print(minint, inputdata[i], maxint)
    i += 1


print(datetime.datetime.today())
print(datetime.date.today())
