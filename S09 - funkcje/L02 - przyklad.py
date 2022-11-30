def WhenEnd():
    from datetime import date

    today = date.today()
    curYear = today.year
    lastDay = date(curYear, 12, 31)

    delta = lastDay - today

    print(delta.days)
    return


WhenEnd()
