#!/usr/bin/python3
from random import randint

class Player:
    def __inti_(self):
        self.dice = []

    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

player1_dice = []
player2_dice = []

print ('player 1 rolled' + str(player1.get_dice()))
print ('player 2 rolled' + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
    print ('draw')
elif sum(player1.get_dice()) < sum(player2.get_dice()):
    print ('player 1 vijeeta')
elif sum(player1.get_dice()) > sum(player2.get_dice()):
    print ('player 2 vijeeta')
