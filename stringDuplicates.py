secret_word = 'aaabbb'
guess = 'a'
xList = list(secret_word)
good_guesses = []
bad_guesses = []       

for letter in range(len(xList)):
    print(xList[letter])
    if guess == xList[letter]:
        good_guesses.append(guess)

print(good_guesses)        