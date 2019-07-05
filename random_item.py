import random

def random_item (chosenWord):
    print('random_item ("',chosenWord,'")')
    xIndex = random.randint(0,(len(chosenWord)-1))
    print("The randomly selected number is {}".format(xIndex))
    xList = list(chosenWord)
    return xList[xIndex]

word_in = 'TreeHouse'
x=random_item(word_in)
print("The return value would be {}".format(x))
