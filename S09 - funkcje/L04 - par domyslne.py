from datetime import date


def PrintAnimal(animal=""):
    if animal == "cat":
        print(
            r"""
|\---/|
| o_o |
 \_^_/"""
        )
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
    elif animal == "":
        print("Add arguments")
    else:
        print("Wrong")
    return


PrintAnimal("cat")
PrintAnimal("b")
PrintAnimal()


def WhenEnd(y=date.today().year, m=date.today().month, d=date.today().day):

    fdate = date(y, m, d)
    lastDay = date(y, 12, 31)

    delta = lastDay - fdate

    print(delta.days)
    return


WhenEnd(2022, 12, 29)
WhenEnd()
