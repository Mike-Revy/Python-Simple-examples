def disemvowel(word):
    disem = list(word)
    vowels = ["a", "A", "e", "E", "i", "I", "o","O", "u", "U"]
    
    for i in range(len(vowels)):
        while True:
            try:
                disem.remove(vowels[i])
            except ValueError:
                break                
                
    return ''.join([i for i in disem])

def disemvowelb(word):
    return ''.join([i for i in word if not i in 'aeiouAEIOU'])
  
  
word = "CaaaPgZZUUiRfseEYooOj"
cipher = disemvowelb(word)
print(word)
print(cipher)