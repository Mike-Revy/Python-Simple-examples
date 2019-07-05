import datetime
from datetime import timedelta

def delorean(num, timeStr):
    if timeStr == "years":
        daycount = num * 365
        return starter + timedelta(days=daycount)
    elif timeStr == "days":
        return starter + timedelta(days=num)
    elif timeStr == "hours":
        return starter + timedelta(hours=num)
    elif timeStr == "minutes":
        return starter + timedelta(minutes=num)
    elif timeStr == "seconds":
        return starter + timedelta(seconds=num)
    else:
        return starter

starter = datetime.datetime(2015, 10, 21, 16, 29)
num = int(input("Enter added time "))
timeStr = str(input("Enter years, days, hours or minutes"))
#timeinc = ["years", "days", "hours", "minutes"]
#pos = timeinc.index(str)

print(starter)
print(delorean(num, timeStr))




