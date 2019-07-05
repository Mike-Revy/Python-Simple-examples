import random
import os
import sys 
    
def get_words():
    word_list = []
    try:
        with open("fruits.txt") as f:
            for line in f:
                # print(line)
                word_list.append(line.strip('\n'))
    except IOError:
        print("can not find file fruits.txt")
        sys.exit()
        
    return(word_list)  
    
def clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')
           
def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('') 
    
    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')
    
    for letter in secret_word:
        if letter in good_guesses:
           print(letter, end='')
        else:
            print('_', end='')
    print('')
 
def get_guess(bad_guesses, good_guesses):
    while True:
        # take a guess 
        guess = input("Guess a letter: ").lower()
        # since all words are lower case ...
        if len(guess) != 1:
            print("You can only guess one letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You already guessed that letter! ")
        elif not guess.isalpha():
            print("you can only try letters !")
        else:
            return(guess)
 
def play(done):
    clear()
    words = get_words()
    secret_word = random.choice(words)
    secret_word_list = list(secret_word)
    print("secret word length {}".format(len(list(secret_word))))
    bad_guesses = []
    good_guesses = []
    
    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)
        
        for i in range(len(secret_word_list)):
            if guess == secret_word_list[i]:
                good_guesses.append(guess)
       
        if len(good_guesses) == len(list(secret_word)):
            print("You win! The word was {}".format(secret_word))
            done = True
        elif guess in secret_word:
            continue
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True
             
        if done: 
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else: 
                sys.exit()

def welcome():                
    print("Welcome to letter Guess!")
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye")
        sys.exit()
    else: 
        return True
    
done = False
while True:
    clear() 
    welcome()
    play(done)
        

