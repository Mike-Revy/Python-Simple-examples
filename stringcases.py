
def stringcases1(inputString):
    low = list(enumerate(inputString.lower()))
    high = list(enumerate(inputString.upper()))
    title = list(enumerate(inputString.title()))
    rev = list(enumerate(inputString[::-1]))
    super = [[low],[high],[title],[rev]]
    return tuple(super)
 
def stringcases2(inputString):
    high = inputString.upper()
    low = inputString.lower()
    title = inputString.title()
    rev = inputString[::-1]
    super = [[high],[low],[title],[rev]]
    return tuple(super) 
 
def stringcases(s):
    return s.upper(), s.lower(), s.title(), s[::-1]

def combo(input1, input2):
    xcombo = []
    for iter in range(len(input1)):
        xnew = (input1[iter],input2[iter])
        xcombo.append(xnew)
    return xcombo
    
#inputString = "abc MY MY hehe"

#print(stringcases(inputString))
x=[1,2,3]
y='abc'
print(combo(x,y))



