data = [
    "Error:File cannot be open",
    "Error:No free space on disk",
    "Error:File missing",
    "Warning:Internet connection lost",
    "Error:Access denied",
]


for line in data:
    print(line.upper())


for line in data:
    elements = line.split(":")
    if elements[0] == "Error":
        print(elements[0].upper(), elements[1].upper())
    else:
        print(elements[0].upper(), elements[1])
