def combiner(my_list):
    words = ""
    sum = 0
    for item in my_list:
        if isinstance(item, (int, float)):
            sum += item 
        elif isinstance(item, str):
            words += item
   
    return words+str(sum)

x = ['apple', 5.2, 'dog', 8]	
outp = combiner(x)
print(outp)	