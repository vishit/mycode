#!/usr/bin/python3

from oop_inheritance import *
import time

swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
swapper_score = 0
loaded_dice_score = 0
total_games = 100000
game_num = 0


print ("simulating.......")

while game_num < total_games :
    swapper.roll()
    loaded_dice.roll()
    swapper.cheat()
    loaded_dice.cheat()

#print ('cheater 1 rolled' + str(swapper.get_dice()))
#print ('cheater 2 rolled' + str(loaded_dice.get_dice()))

    if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
        #print ('draw')
        pass
    elif sum(swapper.get_dice()) < sum(loaded_dice.get_dice()):
        #print ('cheater 1 vijeeta')
        loaded_dice_score += 1
    elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
        #print ('cheater 2 vijeeta')
        swapper_score += 1

    game_num += 1

print ('simulation is over')

print ('final results....drum roll ... ... ...')
time.sleep(3)

print ('WAIT FOR IT --')

if swapper_score > loaded_dice_score :
    print ('\n\nSwapper')
#elif swapper_score == loaded_dice_score :
    #print ('what the deuce, a comet just hit earth')
else:
    print ('\n\n Loaded dice')
