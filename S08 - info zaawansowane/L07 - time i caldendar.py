import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(
    time.perf_counter()
)  # perf_counter - stopwatch - różnica jako licznik czasu wewnątrz programu

import calendar

print(calendar.month(1997, 9, 5, 2))
calendar.setfirstweekday(6)
print(calendar.month(1997, 9, 5, 2))

print(calendar.isleap(2000))

calendar.prcal(2019)
