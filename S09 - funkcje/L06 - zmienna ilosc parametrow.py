from datetime import date


def PrintAnimal(*animal):
    for i in animal:
        if i == "cat":
            print(
                r"""
    |\---/|
    | o_o |
     \_^_/"""
            )
        elif i == "bear":
            print(
                r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
            )
        elif i == "bat":
            print(
                r"""
      /\                 /\
     / \'._   (\_/)   _.'/ \
    /_.''._'--('.')--'_.''._\
    | \_ / `;=/ " \=;` \ _/ |
     \/ `\__|`\___/`|__/`  \/
             \(/|\)/       """
            )
        elif i == "":
            print("Add arguments")
        else:
            print("Wrong")
    return


PrintAnimal("cat", "bat", "rwr")


def WhenEnd(*dates):
    for i in dates:
        lastDay = date(i.year, 12, 31)

        delta = lastDay - i
        print(delta.days)

    return


WhenEnd(date(2022, 12, 29), date.today())
