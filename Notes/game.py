# Pig Game

# Dice class
#   How many sides? - Data Member
#   Method - Roll
# Player class
# Pig class
#   1 or more dice
#   roll
#   return score

import random

class Dice(object):
    def __init__(self, num_sides = 6):
        self.numSides = num_sides

    def Roll(self):
        return random.randint(1, self.numSides)
        
class Pig(object):
    def __init__(self, num_dice = 1, dice_sides = 6):
        self.numDice = num_dice
        self.diceSides = dice_sides
        self.diceList = []
        for i in range(self.numDice):
            self.diceList.append(Dice(self.diceSides))

    def Roll(self):
        scores = []
        for d in self.diceList:
            scores.append(d.Roll())
        return scores

class Player(object):
    def __init__(self, player_name = "New Player"):
        self.name = player_name
        self.score = 0

class Game(object):
    def __init__(self):
        pass

    def addPlayer(self, player_name):
        pass


d = Dice()

p = Pig(10, 20)

print(p.Roll())