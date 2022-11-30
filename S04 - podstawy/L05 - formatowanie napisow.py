# ctrl + b - schowaj sidebar
# ctrl + j - schowaj downbar

hello = "hello %s!"
print(hello % "kate")
print(hello % "chris")

hello = "hello {0:s}"
print(hello.format("kate"))
print(hello.format("chris"))

hello = "%s has %d %s"
print(hello % ("Kate", 1, "animal"))
print(hello % ("Chris", 100000, "$"))

hello = "{0:s} has {1:d} {2:s}"
print(hello.format("Kate", 1, "animal"))
print(hello.format("Chris", 100000, "$"))

line = "{0:20s} costs {1:6d} euro"
print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAWAI", 6))
