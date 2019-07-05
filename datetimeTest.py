import datetime

def time_tango(date_in, time_in):
    return datetime.datetime.combine(date_in, time_in) 
    
def far_away(amt_time):
    return datetime.datetime.now() + amt_time 

def to_string(input):
    return input.strftime('%d %B %Y')

def from_string(input):
    return datetime.datetime.strptime(input, '%m/%d/%y %H:%M')
    
def from_string2(input, form):
    return datetime.datetime.strptime(input, form)
    
#x = datetime.datetime.now()
#print(to_string(x))
#z = "09/24/12 18:30"
#print(from_string(z))
#print('%%%%%%%')  
#f = '%m/%d/%y %H:%M'  
#print(from_string2(z, f ))
#print('%%%%%%%')  
#amt_time = datetime.timedelta(hours=5)
#new_time = far_away(amt_time)
#print(new_time)
datum = datetime.date(2015,12,3) 
zeit = datetime.time(hour=18, minute=30)

print(time_tango(datum, zeit))
