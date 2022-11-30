# import math


# def GiveGeomSeqElement(a1=2, factor=2, index=2):
#     """Funkca licząca wartość ntego elementu ciągu geom."""

#     x = factor ** (index - 1) * a1
#     print(x)

#     return x


# def GiveFactorForGeomSeq(an, an1):

#     x = an1 / an
#     print(x)

#     return x


# def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    
#     x = a1*(1-factor**n)/(1-factor)
#     print(x)
    
#     return x

import geom

geom.GiveGeomSeqElement(3, 4, 3)

for i in range(3, 11):
    geom.GiveGeomSeqElement(3, index=i)

geom.GiveFactorForGeomSeq(12, 24)

geom.GiveSumOfNElementsGeomSeq(2, 3, 4)