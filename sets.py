COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}
def test(targetC):
    print(targetC)
    input(" start test")
    xcheck = set({targetC.pop()})
    while xcheck :
        print(xcheck)
        try :
            xcheck = set({targetC.pop()})
        except KeyError :
            break    


def covers(targetC):
    xList = []
    #try :
    #    xcheck = set({targetC.pop()})
    #except KeyError : 
    #    return xList
        
    for key, value in COURSES.items():
        x = value & targetC
        print(x)
        if value & targetC:
            if key not in xList:
                xList.append(key)
                print(key)
                input(" Key Added ")
    
    # the & operand is bitwise compare - it returns an empty set - or thesubset of the two sets !!! 
    #while xcheck: 
    #    for key in COURSES.keys():
    #        if xcheck.isdisjoint(COURSES[key]) == False:
    #            if key not in xList :
    #                xList.append(key)
    #    try :
    #        xcheck = set({targetC.pop()})
    #    except KeyError :
    #        break
            
    return xList

targetC = ({"Python","functions","Medieval Histroy"})
xList = covers(targetC)
#print(xList)
#targetC = ({"Python","HTML"})
#xList = covers(targetC)
#print(xList)
#targetC = ({"Python"})
#xList = covers(targetC)
#print(xList)
#targetC = ({""})
#xList = covers(targetC)
#print(xList)
#print(type(xList))


    