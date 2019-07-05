fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print(index)
    if index == 0:
        print("check")
        checkStr = fruits[index]
        print(checkStr[0])
        for chkstr in range(len(checkStr)):
            print ("letter :", checkStr[chkstr])
        continue
    else :
        print ("Current fruit :", fruits[index])

print ("Good bye!")