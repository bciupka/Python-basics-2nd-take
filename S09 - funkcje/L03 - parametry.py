def PrintAnimal(animal):
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
    else:
        print("Wrong")
    return


PrintAnimal("cat")
PrintAnimal("bat")
PrintAnimal("bear")


def WhenEnd(y, m, d):
    from datetime import date

    fdate = date(y, m, d)
    lastDay = date(y, 12, 31)

    delta = lastDay - fdate

    print(delta.days)
    return


WhenEnd(2022, 12, 29)
WhenEnd(y=2022, d=28, m=12)
