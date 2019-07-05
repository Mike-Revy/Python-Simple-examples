# regular expressions 
import re 

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(data)
print(re.match(r'Love', data))
# match only matches first item in the string of file - not second 
# print(re.match(r'Kenneth', data))
print(re.search(r'Kenneth', data))

last_name = r'Love'
first_name = r'Kenneth'

# print(data)
print(re.match(last_name, data))
# match only matches first item in the string of file - not second 
# print(re.match(r'Kenneth', data))
print(re.search(first_name, data))

print('*'*10)

print(re.match(r'\w, \w', data))
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
# note addded backslash or escape for ( ) - use escape slashes for wierd URLs!! 

print(re.search(r'\w+, \w+', data))
print(re.search(r'\(\d{3}\) \d{3}-\d{4}', data))
print(re.search(r'\(?\d{3}\)? \d{3}-\d{4}', data))

print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}', data))
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

print(re.findall(r'\w*, \w+', data))

# sets 
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
print('*'*10)
print(re.findall(r'\b[trehous]+\b', data, re.IGNORECASE))
print('*'*10)
print(re.findall(r'\b[trehous]{9}\b', data, re.I))
print('*'*10)
# using negative set example - show emails with no .gov
print(re.findall(r'''
    \b@[-\w\d.]*   # First a word boundry an @ and then any number of chars
    [^gov\t]+  # ignore 1+ instances leters g o v and tab 
    \b # match another word boundry
    ''', data, re.VERBOSE or re.I))

print(re.findall(r"""
    \b[-\w]+, # Find a word boundry, 1+ hyphens or chars, and a coma
    \s # Find 1 whitespace 
    [-\w ]+ # 1+hyphens and chars and EXPLICIT spaces 
    [^\t\n] # Ignore tabs and newlines 
    """, data, re.X))

print('&&&&'*20)
print(re.findall(r'''
    ([-\w ]*,\s[-\w ]+)\t  # Last and first name 
    ([-\w\d.+]+@[-\w\d.]+)\t # Email addresses 
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t   # phone number 
    ([\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (@[\w\d]+)?  # twitter
    ''',data, re.X or re.MULTILINE))

# create a dict out of the data     
print('*'*20)
line = re.search(r'''
    (?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and first name 
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email addresses 
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t   # phone number 
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?  # twitter
    ''', data, re.X or re.M)
    
print(line) 
print(line.groupdict())
 # names = re.match(r'(\b[-\w ]*),\s([\w]+\s[\w]+)', string)
 
string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

#contacts = re.search(r'''
#    ([-\w ]*,\s[-\w ]+),\s  # Last and first name 
#    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s # Email addresses 
#    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?,\s   # phone number 
#    (@[\w\d]+)?  # twitter
#    ''', string, re.X or re.M)
#print(contacts.goupdict()) 
   
contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s # Email addresses 
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?,\s   # phone number 
    ''', string, re.X or re.M)
    
twitters=re.search(r'(@\w+)$',string,re.MULTILINE)
    
line = re.compile(r'''
    (?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first name 
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email addresses 
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t   # phone number 
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?  # twitter
    ''', re.X or re.M)
# removed data and made compile 

print('????'*20)
print(re.search(line, data).groupdict())
print('---'*20)
print(line.search(data).groupdict())
print(':::'*20)
for match in line.finditer(data):
    print(match.group('name'))
print('kkk'*20)
for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))

#players = re.search(r'''
#    (?P<last_name>[-\w ]*),\s(?P<first_name>[-\w]+):\s  # Last and first names
#    (?P<score>[\d]+)
#    ''', string, re.M)   
    
players = re.search(r'''
  (?P<last_name>[\w]+\s?[\w]+?),\s
  (?P<first_name>[\w]+\s?[\w]+?):\s
  (?P<score>[\d]+)
  ''', string, re.M | re.X)
  
class Player:
    last_name = str()
    first_name = str()
    score = str()

    def __init__(self, **players.groupdict()):
    self.last_name = input('last name: ')
    self.first_name = input('first_name: ')
    self.score = input('score: ')
    
print(Player)
contacts = re.match(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s # Email addresses 
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?,\s   # phone number 
    ''', string, re.M)