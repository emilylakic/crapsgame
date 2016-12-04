from tkinter import *

#Represents a display panel for a craps table.
class DisplayPanel:
    
    def __init__(self, parent):
        self.won = 0
        self.lost = 0
        self.point = 0
        labelfont = ('Palatino', 12, 'bold')
        self.t = parent

        self.wonLabel = Label(self.t,text="Won:  \n"+str(self.won),font=labelfont)
        self.wonLabel.pack(side=LEFT)
        
        self.lostLabel = Label(self.t,text="Lost:  \n"+str(self.lost),font=labelfont)
        self.lostLabel.pack(side=RIGHT)

        self.pointLabel = Label(self.t,state=DISABLED,text="Point:  \n",font=labelfont)
        self.pointLabel.pack(side=TOP)

    #Updates win if result = 1, updates lost if result = -1
    #Enables and updates point if result = 0
    def update(self,result,point):
        if(result>0):
            self.won+=1
            self.point=0
            self.wonLabel.config(text="Won:  \n"+str(self.won))
            self.pointLabel.config(state=DISABLED,text="Point:  \n")
        elif(result<0):
            self.lost+=1
            self.point=0
            self.lostLabel.config(text="Lost:  \n"+str(self.lost))
            self.pointLabel.config(state=DISABLED,text="Point:  \n")
        else:
            self.point=point
            self.pointLabel.config(state = NORMAL,text="Point:  \n"+str(self.point),fg = "orange")

    #Opens new final score window
    #Only for when the player closes the main game window
    def scoreWindow(self):
        t= Tk()
        labelfont = ('Times', 15, 'bold')
        finalText = "Number of rolls won: " + str(self.won) +"\n"
        finalText += "Number of rolls lost: " + str(self.lost) + "\n\n"

        #If the player hasn't scored anything and exits the game,
        #no score window is made
        if(self.won==0 and self.lost==0):
            t.destroy()
            return
        
        elif(self.won>self.lost):
            finalText += "You won! Congratulations!!!!!!!!!!!!!!"
            scoreLabel = Label(t, text = finalText, font = labelfont, fg = "green")
        elif(self.won<self.lost):
            finalText += "Better luck next time!"
            scoreLabel = Label(t, text = finalText, font = labelfont, fg = "red")
        else:
            finalText += "It's a draw!"
            scoreLabel = Label(t, text = finalText, font = labelfont, fg = "purple")
        scoreLabel.grid()
        t.mainloop()

    


        
