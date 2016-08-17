import random 
class Dice(object):
    def __init__(self,sides):
        self.sides = sides
    def roll(self):
        faceUp = random.randint(1,self.sides)
        print(faceUp)
six = Dice(6)

six.roll()