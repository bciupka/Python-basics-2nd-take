import os

dirname = r"D:\Projekty\Kursy Python\Python - Beginner\S10 - operacje wejscia i wyjscia\FOLDER\data_output"
filename = r"123.txt"
path =  os.path.join(dirname, filename)

webaddr = []

with open(path, "r") as file:
    for i in file:
        j = i.strip("\n")
        webaddr.append(j)
        if j.endswith(".pl"):
            print(j, "is POLISH")
            with open(os.path.join(os.path.dirname(path), r"webs_pl.txt"), "a") as file1:
                file1.write(i)
        else:
            print(j)
            with open(os.path.join(os.path.dirname(path), r"webs_other.txt"), "a") as file2:
                file2.write(i)
