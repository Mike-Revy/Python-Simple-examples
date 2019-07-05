import re

def first_number (input_string):
    return(re.search(r'\d',input_string))

def numbers(count, in_string):
    search_str = '\d'*count
    return(re.search(search_str,in_string))
    
def phone_numbers(in_number):
    return(re.findall(r'\d{3}-\d{3}-\d{4}',in_number))

def find_words(count, in_string):
    return(re.findall(r'\w{'+str(count)+',}',in_string))

def find_emails(in_string):
    return(re.findall(r'\b[-\w\d.+]+@[-\w\d.]+', in_string))
    
print(phone_numbers('212-345-8976 415-298-9009 303-208-7754'))   
# input_string = 'test12345678'
# print(first_number(input_string))
# print(numbers(4,input_string))
print(find_words(4, "dog, cat, baby, balloon, me"))
print(find_words(6,"123456, Treehouse, student, learn, Kenneth, Python, regex, match, Ryan, g0tcha"))
print(find_emails("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk"))








