import math


def GiveGeomSeqElement(a1=2, factor=2, index=2):
    """Funkca licząca wartość ntego elementu ciągu geom."""

    x = factor ** (index - 1) * a1
    print(x)

    return x


def GiveFactorForGeomSeq(an, an1):

    x = an1 / an
    print(x)

    return x


def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    
    x = a1*(1-factor**n)/(1-factor)
    print(x)
    
    return x
