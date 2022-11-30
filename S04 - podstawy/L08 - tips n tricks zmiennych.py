v1 = 126
v2 = "126"
v3 = 126.0
v4 = "126.0"

print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))

print(v1 + v3, type(v1 + v3))
print(v2 + v4, type(v2 + v4))

print(7 - 1 * 0 + 3 + 3)
print(4**5 / 2**3)
print(2**7)

print(99 + (9 / 9))

a = b = c = 3
c += 2
print(a, b, c)

'''
pyhon odnosi się do zmienną do pamięci a nie przyporządkowuje sztywno pamięci do zmiennej - 100 zmiennych o tej samej wartości będzie zajmować tyle pamięci co 1,
jeżeli któraś z nich zmieni wartość zostanie przyporządkowana do innego zakresu pamięci
'''