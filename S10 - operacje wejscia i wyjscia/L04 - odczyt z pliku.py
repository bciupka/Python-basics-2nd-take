file_path = r"D:\Projekty\Kursy Python\Python - Beginner\S10 - operacje wejscia i wyjscia\FOLDER\data_input\orders.csv"

with open(file_path, "r") as file:
    for l in file:
        l = l.strip("\n")
        order = l.split(",")
        print("Drugstore: {}, Order: {}, Amount: {:d}".format(order[0], order[1], int(order[2])) if len(order)==3 else "NOOOOO")
print("PROCESSING OK")
