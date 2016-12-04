import random

class Die:
    
    def __init__(self):
        self.sides= 6
        self.rollNum = None

    def roll(self):
        self.rollNum = random.randint(1,self.sides)
        return self.rollNum

    def getNumDots(self):
        return self.rollNum

