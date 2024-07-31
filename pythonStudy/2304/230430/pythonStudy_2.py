import time
import datetime
day1 = datetime.date(2019, 12, 14)
day2 = datetime.date(2021, 6, 5)

diff = day2 - day1
print(diff.days)

print(day1.weekday())
print(day1.isoweekday())

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

for i in range(10):
    print(i)
    time.sleep(1)