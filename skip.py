items = ['abc', 'xyz',  'ango']
for index in range(len(items)):
     checkStr = items[index]
     if checkStr[0] == 'a' :
         continue
     else :
        print (items[index])
