
def sillycase(item):
    xMid = int(len(item)/2)
    return(item[0:xMid].lower()+item[xMid:].upper())
    
xWord = "T"
xSilly = sillycase(xWord)
print(xSilly)


        
