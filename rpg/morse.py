class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self):
        morse = []
        for dot in self.pattern:
            print(dot)
            if dot == '.':
                morse.append('dot')
            if dot == '_':
                morse.append('dash')
                
        return '-'.join(morse)
        
    def __iter__(self):
        yield from self.pattern 
        
class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

xmorse = Letter(pattern=['_', '.'])
print (xmorse) 
#test = ['.','-','-']
#x = Letter(pattern=[]) 
#print (str(x))

for k in xmorse.pattern:
    print(k)
    
