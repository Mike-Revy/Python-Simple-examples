import sys
               
def get_words():
    word_list = []
    with open("fruits.txt") as f:
        for line in f:
            # print(line)
            word_list.append(line.strip('\n'))
    
    return(word_list)  
    
words = get_words()
print(words)
