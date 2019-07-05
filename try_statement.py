try:
    x = 1/0
except ZeroDivisionError:
    print("I'm mandatory in this form of try")
    print("Handling ZeroDivisionError")
except NameError:
    print("I'm optional")
    print("Handling NameError")
else:
    print("I'm optional")
    print("I execute if no exception occured")
finally:
    print("I'm optional")
    print("I always execute no matter what")