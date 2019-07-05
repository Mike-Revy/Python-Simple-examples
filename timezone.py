import datetime

import pytz

def to_timezone(zone_str):
    zone_pytz_time = pytz.timezone(zone_str)
    return starter.astimezone(zone_pytz_time)

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))
print(to_timezone('Europe/Paris'))
