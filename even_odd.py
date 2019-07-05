def even_odd(testNumber):
    if testNumber%2 == 0:      #to determine the first factor
        xResult = True
    else:
        xResult = False
    return xResult
		

xNumber = int(input("gimme a number >"))
odd_even_flag = even_odd(xNumber)
print(odd_even_flag)
