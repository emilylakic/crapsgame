from CrapsTable import *
from tkinter import *

#Represents a control panel for a craps "table"
class ControlPanel:
            
    def __init__(self,table,parent):
        self.t = parent
        self.table = table
        labelfont = ('Palatino', 11, 'bold')
        button = Button(self.t, font = labelfont,text = "Roll",fg= "blue", command = lambda: self.rollButton())
        button.pack()
        button.place(anchor=NW)

    #The command for the roll button.
    #Makes the dice roll on the craps table
    def rollButton(self):
        if(not self.table.diceAreRolling()):
            self.table.rollDice()
