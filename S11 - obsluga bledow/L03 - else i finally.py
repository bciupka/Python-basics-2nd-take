import os

line = input("Podaj liczbe ")

filepath = r"D:\Projekty\Kursy Python\Python - Beginner\S11 - obsluga bledow\FOLDER\123.txt"

try:
    with open(filepath, "w") as file:
        file.write(line)
    value = int(line)
except ValueError as e:
    print("sorry", e)
except FileNotFoundError as e:
    print("sorry", e)
except:
    print("Sory, nie pykło")
else:
    print("Success")