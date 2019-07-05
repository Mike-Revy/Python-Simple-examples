
def first_4(item):
	return(item[0:4])
	
def first_and_last_4(item):
	return(item[:4]+item[-4:])

def odds(item):
    return(item[1::2])

def reverse_evens(item):
    if len(item)%2 == 0 :
        return(item[-2::-2])
    else:
        return(item[::-2])
	
xtest = [1,2,3,[45,56],"grapefruit", 85,78,"killroy", 56, 0]
x = first_4(xtest)
print(xtest)
print(x)
y = first_and_last_4(xtest)
print(y)
z = odds(xtest)
print(z)
xNums = [1,2,3,4,5]
k = reverse_evens(xNums)
print(k)
xNums2 = [1,2,3,4,5,6]
l = reverse_evens(xNums2)
print(l)
print(xNums, xNums2)



