from datetime import date


def PrintAnimal(animal=""):
    if animal == "cat":
        print(
            r"""
|\---/|
| o_o |
 \_^_/"""
        )
        result = True
    elif animal == "bear":
        print(
            r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
        )
        result = True

    elif animal == "bat":
        print(
            r"""
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       """
        )
        result = True

    elif animal == "":
        print("Add arguments")
        result = False

    else:
        print("Wrong")
        result = False

    return result


x = PrintAnimal("cat")
print(x)
x = PrintAnimal("b")
print(x)


def WhenEnd(y=date.today().year, m=date.today().month, d=date.today().day):

    fdate = date(y, m, d)
    lastDay = date(y, 12, 31)

    delta = lastDay - fdate

    return delta.days


x = WhenEnd(2022, 12, 29)
print(x)
