def packer(**kwargs):
    print(kwargs)

def part(name=None, **kwargs):
    print(kwargs)

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {} !".format(first_name, last_name))
    else:
        print("Hi no name!")
    
def string_factory(values):
    x=[]
    template = "Hi, I'm {name} and I love to eat {food}"
    for i in range(len(values)):
        xName = values[i]["name"]
        xVal = values[i]["food"]
        x += [template.format(name=xName, food=xVal)]
    return(x)

def unpacker2(course_name=None, minutes=None):
    if course_name and minutes:
        print("Hi {} {} !".format(course_name, minutes))
    else:
        print("Hi no name!")    
    
    
    
#packer(name="Kenneth", num=42, spanish_inquisition=None)

#part(name="Kenneth", num=42, spanish_inquisition=None)  

#unpacker(**{"last_name":"Revy", "first_name" : "Mike"})

# unpacking the tuple course and minutes
    
values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
x = string_factory(values)
print(x)

course_minutes = {"Python Basics": 232, "Django Basics":237, "Flask Basics": 189, "Java Basics": 133}

for course in course_minutes:
    print(course) # print keys 
    print(course_minutes[course]) # print minutes
# keys method !! 
for key in course_minutes.keys():
    print(key)
# value method   
for values in course_minutes.values():
    print(values)
# Tupple method (items)
# unpacking the tuple course and minutes
for course, minutes in course_minutes.items():    
    print(" {} is {} minutes long".format(course,minutes))
# enumerate - takes an ordered iterable - list or string or tuple 
# returns a tuple with index and item) 
list(enumerate("abc")) # [(0, 'a'), (1, 'b'), (2, 'c')]
for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print("{}: {}".format(index+1,letter))
    
    
    



