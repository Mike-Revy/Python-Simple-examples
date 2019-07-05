#>>> from characters import Thief
#>>> mike = Thief()
#>>> mike.sneaky
#True
#>>> Thief.sneaky
#True
#>>> mike.sneaky = False
#>>> mike.sneaky
#False
#>>> del mike

#>>> mike = Thief
#>>> mike
#<class 'characters.Thief'>
#>>> mike = Thief("Mike", False)
#>>> mike
#<characters.Thief object at 0x000001E781CB7588>
#>>> mike.name
#'Mike'
#>>> mike.sneaky
#False
#>>> exit()

#>>> from characters import Thief
#>>> mike = Thief("Mike", scars= None, favorite_weapon = "Wit")
#>>> print(mike)
#<characters.Thief object at 0x0000021E3513B320>
#>>> mike.favorite_weapon
#'Wit'

import random

class Character: 
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items(): 
            setattr(self, key, value)
            

class Thief(Character):
    # inherited from superclass Character
    sneaky = True
    
    def __init__(self, name, sneaky=True, **kwargs):
        # setting globals for subclass - super 
        super().__init__(name, **kwargs)
        self.sneaky = sneaky
        
    
    def pickpocket(self):
        # print("Called by {}".format(self)) 
        if self.sneaky:
            return bool(random.randint(0,1))
        return False 
        # return bool(random.randint(1,1))
        # OR return self.sneaky and bool(random.randint(0, 1))
        
    def hide(self, light_level):
        return self.sneaky and light_level < 10
            
class Student:
    name = "Mike"
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.reassurance()        


            
