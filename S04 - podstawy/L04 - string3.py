zmienna = """
Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and influence, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]

Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, including Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.

At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution To Cinema. In 1998, they were awarded the AFI Star Award by the American Film Institute. Many sketches from their TV show and films are well-known and widely quoted. Both Holy Grail and Life of Brian are frequently ranked in lists of greatest comedy films. In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]
"""

print(zmienna.upper())
print(zmienna.lower().replace("monty", "flying"))
print(zmienna.split(" "))

print("python appears", zmienna.lower().count("python"))
print(r"to print the \ you need to put \ twice in your text like this: \\")
print("The best hits of '80s!!!")

amountPLN = 234
print("cur", "\texchange", "amount")
print("USD", 3.65, amountPLN / 3.65, sep="\t")
print("EUR", 4.23, amountPLN / 4.23, sep="\t")

valAsText = "123.45"
factor = 1.23

print(
    "value is",
    valAsText,
    "factor is",
    factor,
    "value*factor=",
    float(valAsText) * factor,
)

# Shift + ctrl + space - toggle parameter hint
# ctrl + / - comment
# ctrl + alt + n - run
# shift + alt + F - black
# ctrl + d - znajdz to samo i dodaj kursor
# alt + strzalki - ruszanie linia
# alt + shift + strzalki - kopiuj linie
# cltr + l - zaznacz linie