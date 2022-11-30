import sys

file_path = (
    r"D:\Projekty\Kursy Python\Python - Beginner\S11 - obsluga bledow\FOLDER\orders.csv"
)

with open(file_path, "r") as file:

    for line in file:
        try:
        
            line = line.replace("\n", "")
            order = line.split(",")

            name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' % (name, item, amount))
        
        except:
            print(line)
            print("BŁĄD", sys.exc_info()[0])
        

print("Processing finished")
