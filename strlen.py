def just_right(testString):
    if len(testString) < 5:      #to determine the first factor
        return("Your string is too short")
    elif len(testString) > 5:
        return("Your string is too long ")
    else:
        return(True)

xString = input("gimme a string >")
okString = just_right(xString)
print(okString)