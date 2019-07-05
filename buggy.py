# import pdb

def something_silly(arg1, arg2):
    if len(arg1) > len(arg2):
        # Import and use PDB here
        import pdb; pdb.set_trace()
        arg1[0] = arg2[0]
    return arg1, arg2

# my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

# pdb.set_trace()

# import pdb; pdb.set_trace()

# del my_list[3]
# del my_list[3]
# del my_list[4]
# print(my_list)

# keywords in pdb - next .. runs line of code indicated, q - quit C - continue 
# Zen of Python - nice code .. import this 

