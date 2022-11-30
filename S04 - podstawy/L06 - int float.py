name = "Bartek"
age = 24
daysInYear = 365
message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name, age, age * daysInYear))

a = 1234567890
b = 12345
message2 = "%d divided by %d is %d and the rest is %d"
print(message2 % (a, b, a // b, a % b))
