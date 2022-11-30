# zad 1

initialCapital = 20000
percent = 0.03
maxTime = 10

i = 0
tmp = 0
capital = initialCapital
while i < 10:
    capital *= 1 + percent
    i += 1
    print("{}\tKwota: {:.2f}".format(i, capital))
print("Cały zarobek = {:.2f}".format(capital - initialCapital))

# zad 2

number = 20730906
numbers = list(str(number))
tmp = 0
for i in numbers:
    tmp += int(i)
print(tmp, i)  # i nie "znika" po pętli for


tmp = j = 0
while j < len(str(number)):
    tmp += int(str(number)[j])
    j += 1
print(tmp)


tmp = 0
numberCopy = number
while numberCopy != 0:
    tmp += numberCopy % 10
    numberCopy //= 10
print(tmp)

# zad 3


lenght = 6
text = """United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier."""

text = text.replace("\n", " ")
amount = i = count = 0

while i < len(text):
    if text[i] != " ":
        count += 1
        if count == lenght + 1:
            amount += 1
        i += 1
    else:
        count = 0
        i += 1
print(amount)


words = text.split(" ")
long = short = i = 0
while i < len(words):
    if len(words[i]) > lenght:
        long += 1
        i += 1
    else:
        short += 1
        i += 1
print(short, long)

print(round(45.21414, 2)) # round(liczba, ilosc po przeciku) w przykładzie, ja użyłem formatu {:.2f}