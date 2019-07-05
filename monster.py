# class Monster(object):
# must be capital .. object specifies all inheritance of class object - but in python 3 this is implied 
import random 
# imports do not need to be inside a class - but if used in the class need to be in the import library 
# PEP 8 rule - leave 2 blank lines after naming a global constant 

from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']

# adding Combat passed to Monster makes all subclasses have combat 

class Monster(Combat): 
    # default attributes - can be overwritten
    # hit_points = 1
    # color = 'yellow'
    # weapon = 'sword'
    # sound = 'roar'
    # use dunder init to initialize attributes 
    # from monster import Monster
    # slimey = Monster(5, 'sword', 'blue', 'glug')
    # def __init__(self, hit_points, weapon, color, sound):
    # def __init__(self, hit_points=5, weapon="dunderblus", color="black", sound="squark"):
    #    self.hit_points = hit_points
    #    self.weapon = weapon
    #    self.color = color
    #    self.sound = sound 
    # ** means getting a dict - so keywords and value
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'
    
    def __init__(self, **kwargs):
        #self.hit_points = kwargs.get('hit_points', 1)  
        # trys to find key value - none if not found - override with 1
        #self.weapon = kwargs.get('weapon', 'sword')
        #self.color = kwargs.get('color', 'yellow')
        #self.sound = kwargs.get('sound', 'roar') 
        # example : jubjub = Monster(color = 'red', sound = 'tweet')
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)
        self.score = (2,1)  # tuple 
        # Below is how to set attributes - other than initial values  
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __str__(self):
        # return 'Player 1:{}; Player2:{}'.format(*self.score) unpack tuple with *
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points, 
                                              self.experience)
                                              
    def battlecry(self):
        return self.sound.upper()

        # create a subclass of Monster 
class Goblin(Monster):
    # pass  # tells python to move on .. 
    # to instantiate a subclass must import Goblin 
    # OR import monster .. then x = monster.Goblin()
    max_hit_points = 3
    max_experience = 2
    sound = 'squeek'
    
class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'

class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaaar'   
# in python - from monster import Monster
# Monster.hit_points .. 1     
# attributes are NOT functions - so no () to be caleld 

# to call a mthod must create an instance 
#jubjub = Monster()
#jubjub.sound()
#>> 'ROAR'
#jubjub.sound = 'tweet'
#jubjub.sound() 
#>> 'TWEET'

## __init__ called dunder init
 
class Student:
    name = "Michael Revy"

# to create an instance ... mike = Student() 
# mike.name = "Kilroy"
# etc etc 
# attributes are ok .. but can also addd functions - methods 

# Keeping code dry - do not repeat code 
# Group common operations into functions 
# group common functionality into classes 
#