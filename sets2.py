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
def covers(targetC):
    xList = []
    for key, value in COURSES.items():
        if len(targetC)==len(value & targetC):
            if value & targetC:
                if key not in xList:
                    xList.append(key)
            
    return xList

    
targetC = ({"Python","functions","Medieval Histroy"})
targetC = ({"conditions","input"})
xList = covers(targetC)
print(xList)

