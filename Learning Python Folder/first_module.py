# For module1

import random

class Dice():
    def __init__(self,dice_side = 6): 
        self.num_sides = dice_side

def roll(self):
    return random.randint(1,self.num_sides)

# For module2

sixSided = Dice()
print(sixSided)
for _ in range(10):
    print(sixSided.roll(), end=" ")

