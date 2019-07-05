import random
def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    if num == 0:
        return not num % 2
    elif num % 2 == 0:      
        return True
    else:
        return False    

start = 5
while start:
    num = random.randint(1,99)
    if even_odd(num):
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
    start=start-1
