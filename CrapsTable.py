from tkinter import *
from RollingDie import *
from App import*

class CrapsTable(Frame):
    def __init__(self, parent):
        self.die1 = RollingDie()
        self.die2= RollingDie()
        self.delay = 20
        self.clock = App()
        self.game = CrapsGame()
        self.display = DisplayPanel(parent)

    def CrapsTable(display):
        root = Tk()
        root.configure(background='green')
        widget.config(highlightbackground='Orange')

    def rollDie(self):
        RollingDie.setBounds(-3, 3, 3, -3)
        self.die1.roll()
        self.die2.roll()
        self.clock.start()
    def actionPerformed():
        if(isDiceRolling()):
            if(!self.clock.isRunning()):
                self.clock.restart()
            if(self.die1.isRolling()):
                self.die1.avoidCollision(die2)
            elif(self.die2.isRolling()):
                self.die2.avoidCollision(die1)
            else:
                self.clock.stop()
                total = die1.getNumDots() + die2.getNumDots()
                result = game.processRoll(total)
                point = game.getPoint()
                display.update(result, point)
        repaint()

    def isDiceRolling(self):
        return self.die1.isRolling() or self.die2.isRolling()

    #def paintComponent():
    #    super.paintComponent()
    #    die1.draw(g);
    #    die2.draw(g);
