def PrintCat():
    # this function prints a cat
    print(
        r"""
|\---/|
| o_o |
 \_^_/"""
    )
    return


def PrintBear():
    """
    This function prints a bear
    """
    print(
        r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    )
    return


def PrintBat(times):
    """This function prints a bat

    Args:
        times (integer): How many times a bat will be printed
    """
    print(
        times
        * r"""
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       """
    )
    return


PrintCat()
PrintBear()
PrintBat(2)
