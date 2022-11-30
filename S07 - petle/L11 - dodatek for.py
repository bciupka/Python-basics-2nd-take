tmp = 0
for i in range(20):
    print(i, tmp)
    tmp = i + (i + 1)

text = """Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t."""

words = text.replace("\n", " ").split(" ")
for i in words:
    if "p" in i.lower():
        print(i)

dictionary = {"A": "80%-100%", "B": "60%-80%", "C": "50-60%", "D": "less then 50%"}

for i in dictionary:
    print("{} - {}".format(i, dictionary[i]))

listOfWords = {}
words = text.replace("\n", " ").lower().split(" ")

for i in words:
    if listOfWords.get(i) == None:
        listOfWords.setdefault(i, 1)
    else:
        listOfWords.update({i : listOfWords[i]+1})
        
print(listOfWords)