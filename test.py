import datetime

time = datetime.datetime.now()
days = datetime.timedelta(30)
newdate = time-days
print(time)
print(days)
print(newdate)