favorite_things =["raindrops on roses", "whiskers on kittens", "bright copper kettles"]
favorite_things + ["warm woolen mittens"]
# + is temporary add - make permanent, use +=
favorite_things += ["warm woolen mittens"]
# if u use += then give it a list, append requires only string - already knows it is a list 
favorite_things.append(["bright paper packages tied with string"])
del favorite_things[-1]
favorite_things.append("bright paper packages tied with string")
# extend requires a list to be passed in 
favorite_things.extend(["cream colored ponies","crisp apple strudels"])
# more interesting .. .
a = [1,2,3]
a.extend("abc")
# gives u [1, 2, 3, 'a', 'b', 'c']
del favorite_things[1]
# insert takes startposition, then string - not list
favorite_things.insert(1,"whiskers on kittens")
alpha_list = [1, 1, 2, 3, 4]
alpha_list.remove(1)
# remove and not del will remove 1st instance of search value
# remove has ValeError when searched for item is not found .. can use with try in a loop
names = ["Kenneth", "Alena", "Sam", "Amjith"]
name_1 = names.pop()
# name_1 .. Amjith - no args, pop takes LAST item 
name_2 = names.pop(0) 
# name_2 -- Kenneth
# using .sort ..
sorted = unsorted
sorted.sort()
# BOTH sorted and unsorted WILL BE THE SAME!! 
sorted = unsorted[:]
sorted.sort() 
# above is how it is done . must use slices .. my guess is otherwise bot variables us same memory
numbers = list(range(20))
# step argument is second colon - [start, stop, step] 
numbers[::2]
numbers[1:5:2]
numbers[::]
numbers[2::2]
# nota bene 
numbers[2:2] - [] # NOT element in position 2!! 
"Oklahoma"[::2] # Olhm -
numbers[-2:]
numbers[-2:-5] # slice moves ONLY left to right BUT 
numbers[-2:-5:-1] # 18, 17, 16 
numbers[::-1]
# strings in python are iterable, but NOT immutable
# thus need to use more lists 
rainbow = ["red","orange","green","yellow","blue","black","white","aqua","purple", "pink"]
# using slices to delete things - inclusive 1st element Excluding last
# OR - forget 0 as first index .. delete 6th,7th and 8th element 
del rainbow[5:8]
# reverse order of things using slices 
rainbow[2:4]= ["yellow", "green"]
# add an item - indigo - specify the spot and add 
rainbow[4:5] = ["blue", "indigo"]
rainbow[-2:] = ["violet"]
# if you made a mistake and added a string 
rainbow[-2:] = "violet"
rainbow[-6:] = ["".join(rainbow[-6:])]
for i in range(rainbow[5:6])
    print(i)








