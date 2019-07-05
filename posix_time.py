import time
import datetime
from datetime import timedelta

def minutes(time1, time2):
    return ((time2 - time1)/ timedelta(minutes=1))
    
    
def timestamp_oldest(*args):
    args = list(args)
    # new_list = sorted(args, reverse=True)
    new_list = sorted(args)
    return datetime.datetime.fromtimestamp(new_list[0])
            
posix_list = []
for _ in range(10):
    posix_list.append(time.time())

posix_now = time.time()
starter = datetime.datetime(2015, 10, 21, 16, 29)
starter2 = starter + timedelta(seconds=20)

d = datetime.datetime.fromtimestamp(posix_now)
no_microseconds_time = time.mktime(d.timetuple())
has_microseconds_time = time.mktime(d.timetuple()) + d.microsecond * 0.000001

#print (posix_now)
#print (no_microseconds_time)
#print (has_microseconds_time)
#print(d)
#print("*************************")
print(timestamp_oldest(posix_list[0], posix_list[1], posix_list[2]))
# print(minutes(starter, starter2))



