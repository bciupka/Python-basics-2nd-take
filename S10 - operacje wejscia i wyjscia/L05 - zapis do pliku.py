import os

webaddr = []
line = input("Adres strony")
while line:
    webaddr.append(line)
    line = input("Adres strony")

dirname = r"D:\Projekty\Kursy Python\Python - Beginner\S10 - operacje wejscia i wyjscia\FOLDER\data_output"
filename = input("Nazwa pliku")

path = os.path.join(dirname, filename+".txt")

with open(path, "w") as file:
    for i in webaddr:
        file.write(i + "\n")
