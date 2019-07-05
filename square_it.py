
def maybe_int(s):
    try:
        return int(s)*int(s)
    except ValueError:
        iterations = len(s)-1
        xString = s
        for i in range(iterations) :
            xString = xString + s
            
        return xString

def str_square(s):
    iters = len(s)-1
    xString = s
    for i in range(iters) :
        xString = xString + s
         
    return xString
        
        
#lst = [maybe_int(s) for s in lst]
test = maybe_int(5)
print(test)
test = maybe_int("2")
print(test)
test = maybe_int("tim")
print(test)
# ValueError