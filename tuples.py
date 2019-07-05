# tuples - lists - immutable
# lists - [,]  dictionaries {:} strings "" or ''
my_tuple = (1,2,3) 
# (1,2,3)
my_second_tuple = 1,2,3   
# (1,2,3)
my_third_tuple = (5,) 
# (5,) - this way you know it is a tuple
my_fourth_tuple = tuple([1,2,3])
dir(my_tuple) 
# directory of methods?? 
# may change mutable items inside of a tuple
tuple_with_a_list = (1, "apple", [3,4,5])
# numbers and strings immutable - but list is mutable 
tuple_with_a_list[2][1] = 7
# may not remove the list though ... 
a = 5
b = 20
a, b = b, a
a = 5
b = 20 
c = b, a  
# look at c
# python can pack unpack .. just unpacks to variableson the left of = 
a , b = b, a

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
    
print(add(5,5))

# 10

def add2(base, *args):
    total = base
    for num in args:
        total += num
    return total
    
print(add2(2,5,34))

def multiply(*nums):
    total = 0
    init = 0
    for num in nums:
        if init == 0:
            total = num
            init += 1
        else:
            total *= num
    return total
    
print(multiply(3,3,3,4))
print(multiply(3,3,3,0))


