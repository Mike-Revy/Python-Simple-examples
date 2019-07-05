"""Dungeon Game 
Explore a dungeon to find a hidden door and escape. But be careful!
the grue is hiding somewhere inside ! 

Created 2017
Update 2017
Author: Mike Revy
"""

import logging 
import os 
import random

# draw grid 
# pick a random location for the player 
# pick a random location for the exit door 
# pick a random location for the monster 
# draw the player in the grid
# take input for movement 
# move player, unless invalid move (past edges of the grid)
# check for win or loss 
# clear the screen and redraw grid

#logging.info("You won't see this")
#logging.warn("OH NO")
# 6 Log levels - Critical, Error, Warning, Info, Debug, Notset

logging.basicConfig(filename='game.log', level=logging.DEBUG)
logging.critical("message")
logging.error("message")
logging.warning("message")
logging.info("message")
logging.debug("message")

CELLS = [ (0,0), (1,0), (2,0), (3,0), (4,0),
          (0,1), (1,1), (2,1), (3,1), (4,1),
          (0,2), (1,2), (2,2), (3,2), (4,2),
          (0,3), (1,3), (2,3), (3,3), (4,3),
          (0,4), (1,4), (2,4), (3,4), (4,4) ]
          
# each item in the grid is a tuple for coordinates in the grid and entire thing is a list

def build_cells(width, height):
    """build_cells - return a width x height grid of two tuples
       
    >>> cells = build_cells(2,2)
    >>> len(cells)
    12
       
    """
    cells=[]
    for y in range(height):
        for x in range(width):
            cells.append((x,y))
    return cells
    

def matrix_build():
    dimension = int(input("Give matrix dimension (start is at ZERO - so 1 dimension is 00,10,01,11)"))
    matrix = []
    if dimension > 0 :
        x=0
        while x <= dimension:
            y = 0
            while y <= dimension: 
                matrix.append((y,x))
                y +=1
            x +=1
    return matrix, dimension

def move(player, direction, max):
    # max = 9
    # solution to code challenge where inflict pain on bad move 
    x, y, hp = player
    xDir, yDir = direction
    x = x + xDir
    y = y + yDir
    if y < 0:
        hp -= 5
        y = 0
    if y > max:
        hp -= 5
        y = max
    if x < 0:
        hp -= 5
        x = 0
    if x > max:
        hp -= 5
        x = max
    return x,y,hp
    


def clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')

def get_locations(matrix):
    """Randomly pick starting locations for the monster, the door, and the player"""
    # function returns tuple 
    # return random.sample(CELLS,3)
    return random.sample(matrix,3)
    # returns 3 UNIQUE random samples 

def move_player(player, move):
    # get the player's location
    x,y = player
    if move == "LEFT" :  # LEFT,  y-1
        x = x-1
    if move == "RIGHT" : # RIGHT, y+1
        x = x+1
    if move == "UP" :    # UP  x-1
        y = y-1
    if move == "DOWN" :  # DOWN x +1
        y = y+1
    return x, y

def get_moves(player, dimension): 
    # moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x,y = player  # unpack player tuple 
    moves = []
    if y != 0 : 
        moves.append("UP")
    if y < dimension :  
        moves.append("DOWN")
    if x != 0 : 
        moves.append("LEFT")
    if x < dimension :  
        moves.append("RIGHT")
    return moves    

def draw_map(player, matrix, dimension):
    print(" _"*(dimension+1))
    tile = "|{}"
    for cell in matrix:
        x, y = cell
        if x < dimension:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else: 
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else: 
                output = tile.format("_|")
        print(output, end = line_end)
                                              
def game_loop(matrix, dimension):

    monster, door, player = get_locations(matrix)
    logging.info('monster: {}; door: {}; player: {}'.format(monster, door, player))
    playing = True
    
    while playing: 
        draw_map(player, matrix, dimension)
        moves = get_moves(player, dimension)
        print("You're currently in room {}".format(player))  
        if player == monster :
            print("You found the MONSTER")
            playing = False
        elif player == door :
            print("You found the door an FREEDOM")
            playing = False
        else :
            print("You can move {}".format(", ".join(moves))) # fill with available moves
            print ("Enter QUIT to quit")
            move = input(">")
            move = move.upper()
    
            if move == 'QUIT':
                break
            elif move in moves :
                player = move_player(player, move)
                clear()
            else : 
                input("invalid move")    
            clear()
    else: 
        # on break this else NOT executed ... on plying == False gets executed
        if input("Play again [Y/n]").lower() != "n":
            clear()
            matrix, dimension = matrix_build()
            game_loop(matrix, dimension)
            
# EXAMPLES:
#x,y,hp = move((1, 1, 10), (-1, 0)) 
#print(x,y,hp) # => (0, 1, 10)
#x,y,hp = move((0, 1, 10), (-1, 0)) 
#print(x,y,hp) # => (0, 1, 5)
#x,y,hp = move((0, 9, 5), (0, 1)) 
#print(x,y,hp) # => (0, 9, 0)
#print("Monster in room {}".format(monster)) 
#print("Door in room {}".format(door)) 
#python -m doctest dungeon_game.py
#width = 1
#height = 2
#cellophane = build_cells(width, height)
   
print("Welcome to the dungeon!")    
input("Press return to start!")
clear()
matrix, dimension = matrix_build()
game_loop(matrix, dimension)
    

    
    