from Die import *
from tkinter import *
import random

#Implements a rolling die

class RollingDie(Die):
    #Sets this die off the table
    def __init__(self):
        self.xCenter = -1
        self.yCenter = -1
        self.xSpeed = 0
        self.ySpeed = 0
        self.sides = 6
        self.tableLeft = 0
        self.tableRight = 0
        self.tableTop = 0
        self.tableBottom = 0
        self.slowdown = 0.97
        self.speedFactor = 0.04
        self.speedLimit = 2.0
        self.dotSize = 0
        self.dieSize = 24

        
    #Sets the table boundaries
    def setBounds(self,left, right, top, bottom):
        self.tableLeft = left
        self.tableRight = right
        self.tableTop = top
        self.tableBottom = bottom

    #Starts this die rolling
    def roll(self):
        super().roll()
        width = self.tableRight - self.tableLeft
        height = self.tableBottom - self.tableTop
        self.xCenter = self.tableLeft
        self.yCenter = self.tableTop + height / 2
        self.xSpeed = width * (random.randrange(0.0,1.0)+1) * self.speedFactor
        self.ySpeed = height * (random.randrange(0.0,1.0)-.5) * 2.0 * self.speedFactor

    #Returns true if this die is rolling, otherwise returns false
    def isRolling(self):
        return self.xSpeed > self.speedLimit or self.xSpeed < -self.speedLimit or self.ySpeed > self.speedLimit or self.ySpeed < -self.speedLimit

    #Keeps moving this die as long as it overlaps with other
    def avoidCollision(self,other):
        if(other == self):
            return
        while(abs(self.xCenter - other.xCenter) < self.dieSize and abs(self.yCenter - other.yCenter) < self.dieSize):
            self.move()

    #Moves this dice on the table and bounces off the edges when necessary
    def move(self):
        self.xCenter = self.xSpeed
        self.yCenter = self.ySpeed
        radius = self.dieSize / 2
        if(self.xCenter < self.tableLeft + radius):
            self.xCenter = self.tableLeft + radius
            self.xSpeed = -self.xSpeed
        if(self.xCenter > self.tableRight - radius):
            self.xCenter = self.tableRight - radius
            self.xSpeed = -self.xSpeed
        if(self.yCenter < self.tableTop + radius):
            self.yCenter = self.tableTop + radius
            self.ySpeed = -self.ySpeed

    #Draws this die, rolling or stopped; also moves this die, when rolling
    def draw(self):
        if(self.xCenter < 0 or self.yCenter < 0):
            return
        elif(self.isRolling()):
            self.move()
            self.drawRolling()
            self.xSpeed *= self.slowdown
            self.ySpeed *= self.slowdown
        else:
            self.drawStopped()

    def drawDie(self, x1, y1, x2, y2, r):
        self.create_arc(x1, y1, x1+r, y1+r, start=90, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_arc(x2-r, y1, x2, y1+r, start=0, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_arc(x1, y2-r, x1+r, y2, start=180, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_arc(x2-r, y2-r, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_rectangle(x1+r/2, y1-r/2, x2-r/2, y2+r/2, fill = "red")
        self.create_rectangle(x1, y1, x2, y2, fill="red")

    #Draws this die when rolling with a random number of dots
    def drawRolling(self):
        x = self.xCenter - self.dieSize/2 + int(random.randrange(0,3))
        y = self.yCenter - self.dieSize/2 + int(random.randrange(0,3))
        if(x%2 != 0):
            self.drawDie(x,y,x+self.dieSize,y+self.dieSize, self.dieSize)
        else:
            oval = canvas.create_oval(x-2,y-2,x+self.dieSize+4,y+self.dieSize+4)
        die = Die();
        die.roll()
        self.drawDots(x, y, Die.getNumDots())

    #Draws this die when stopped
    def drawStopped():
        x = self.xCenter - self.dieSize/2
        y = self.yCenter - self.dieSize/2
        self.drawDie(x, y, x+self.dieSize, y+self.dieSize)
        self.drawDots(x, y, self.getNumDots())

    #Draws a given number of dots on this die
    def drawDots(self, x, y, numDots):
        self.setFill("White")
        self.dotSize = self.dieSize/4
        step = self.dieSize/8
        x1 = x + step - 1
        x2 = x + 3*step
        x3 = x + 5*step + 1
        y1 = y + step - 1
        y2 = y + 3*step
        y3 = y + 5*step + 1

        #Insert a replacement for a switch
        v = numDots
        for case in switch(v):
            if case(1):
                #Make 1 Dot
                oval1 = canvas.create_oval(x2, y2, x2+self.dotSize, y2+self.dotSize)
                break
            if case(2):
                #Make 2 Dots
                oval1 = canvas.create_oval(x1, y1, x1+self.dotSize, y1+self.dotSize)
                oval2 = canvas.create_oval(x3, y3, x3+self.dotSize, y3+self.dotSize)
                break
            if case(3):
                #Make 3 Dots
                oval1 = canvas.create_oval(x1, y3, x1+self.dotSize, y3+self.dotSize)
                oval2 = canvas.create_oval(x2, y2, x2+self.dotSize, y2+self.dotSize)
                oval3 = canvas.create_oval(x3, y1, x3+self.dotSize, y1+self.dotSize)
                break
            if case(4):
                #Make 4 Dots
                oval1 = canvas.create_oval(x1, y1, x1+self.dotSize, y1+self.dotSize)
                oval2 = canvas.create_oval(x3, y1, x3+self.dotSize, y1+self.dotSize)
                oval3 = canvas.create_oval(x1, y3, x1+self.dotSize, y3+self.dotSize)
                oval4 = canvas.create_oval(x3, y3, x3+self.dotSize, y3+self.dotSize)
                break
            if case(5):
                #Make 5 Dots
                oval1 = canvas.create_oval(x1, y1, x1+self.dotSize, y1+self.dotSize)
                oval2 = canvas.create_oval(x3, y1, x3+self.dotSize, y1+self.dotSize)
                oval3 = canvas.create_oval(x2, y2, x2+self.dotSize, y2+self.dotSize)
                oval4 = canvas.create_oval(x1, y3, x1+self.dotSize, y3+self.dotSize)
                oval5 = canvas.create_oval(x3, y3, x3+self.dotSize, y3+self.dotSize)
                break
            if case(6):
                #Make 6 Dots
                oval1 = canvas.create_oval(x1, y1, x1+self.dotSize, y1+self.dotSize)
                oval2 = canvas.create_oval(x3, y1, x3+self.dotSize, y1+self.dotSize)
                oval3 = canvas.create_oval(x1, y2, x1+self.dotSize, y2+self.dotSize)
                oval4 = canvas.create_oval(x3, y2, x3+self.dotSize, y2+self.dotSize)
                oval5 = canvas.create_oval(x1, y3, x1+self.dotSize, y3+self.dotSize)
                oval6 = canvas.create_oval(x3, y3, x3+self.dotSize, y3+self.dotSize)
                break

def main():
    rolling = RollingDie()
    rolling.roll()
    rolling.isRolling()

main()

    
