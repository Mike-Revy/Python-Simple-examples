# usings sets in python 
# old way - 
set([1,3,5])
type({})  # empty set will give you type dict 
# <class 'dict'>
type(set())
# <class 'set'>
# sets are UNSORTED 
low_primes = {1,3,5,7,11,13}
# to add an item - add 
low.primes.add(17)
low_primes.update({19,23},{2,29})
low_primes.add(15)
low_primes
low_primes.remove(15)
low_primes.remove(199)  # KeyError: 199
# can use method discrad - no KeyErro triggered
low_primes.discard(199)
while low_primes:
    print(low_primes.pop()/3)
    
set1 = set(range(10))
set2 = {1,2,3,5,7,11,13,17,19,23}
set1.union(set2)
# use the pipe character .. do not hav on my keyboard
# set1 ¦ set2
set1.difference(set2)
set1 - set2
# symetric difference ^
set1 ^ set2
set2.symmetric_difference(set1)
set1.intersection(set2,set1)
set1 & set2
