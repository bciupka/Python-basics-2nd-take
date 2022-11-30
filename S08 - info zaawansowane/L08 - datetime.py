import datetime

print(datetime.date.today())
delta = datetime.timedelta(7)
print(datetime.date.today() + delta)
print(datetime.datetime.today() + delta)
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.now().weekday())

print(datetime.datetime.now().strftime("%w %a %A %d.%m.%Y %H:%M:%S.%f"))
