from CrapsTable import *
from tkinter import *

#Represents a control panel for a craps "table"
class ControlPanel:
            
    def __init__(self,table,parent):
        self.table = table
        self.t = parent
        button = Button(self.t, text = "Roll", command = lambda: self.rollButton())
        button.pack()

    def rollButton(self):
        if(not self.table.diceAreRolling()):
            self.table.rollDice()

