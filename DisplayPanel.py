from tkinter import *
import json

#Represents a display panel for a craps table.
class DisplayPanel:

    def __init__(self, parent):
        #load the current game data in json format from a configuration file
        initData = self.loadConfigData()

        self.won = initData["won"]
        self.lost = initData["lost"]
        self.point = 0
        labelfont = ('Palatino', 12, 'bold')
        self.t = parent

        self.wonLabel = Label(self.t,text="Won:  \n"+str(self.won),font=labelfont)
        self.wonLabel.pack(side=LEFT)

        self.lostLabel = Label(self.t,text="Lost:  \n"+str(self.lost),font=labelfont)
        self.lostLabel.pack(side=RIGHT)

        self.pointLabel = Label(self.t,state=DISABLED,text="Point:  \n",font=labelfont)
        self.pointLabel.pack(side=TOP)

    # Load the current game status from a configuration file
    def loadConfigData(self):
        inFile = open("Craps.config", "r")
        data = json.load(inFile)
        inFile.close()
        return data  

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

    #Opens new final score window when the player closes the main game window
    def scoreWindow(self):
        # Position the window to the center of screen 
        def centerWindow():
            w = 250
            h = 150

            sw = t.winfo_screenwidth()
            sh = t.winfo_screenheight()

            x = (sw - w)/2
            y = (sh - h)/2
            t.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Writes the game status to a configuration file
        def writeToFile(data):
            outFile = open('Craps.config', 'w')
            json.dump(data, outFile)
            outFile.close()
        
        # Set the current game status and save to a file
        def saveGame():
            gameStatus = {"won": self.won, "lost": self.lost } 
            writeToFile(gameStatus)
            t.destroy()

        # Reset/Erase game status and save to a file
        def exit():
            gameStatus = {"won": 0, "lost": 0 } 
            writeToFile(gameStatus)
            t.destroy()

        t = Tk()
        t.wm_title("Game Stats")
        labelfont = ('Times', 15, 'bold')
        finalText = "Number of rolls won: " + str(self.won) +"\n"
        finalText += "Number of rolls lost: " + str(self.lost) + "\n\n"

        #If the player hasn't scored anything and exits the game,
        #no score window is made
        if(self.won==0 and self.lost==0):
            t.destroy()
            return
        elif(self.won>self.lost):
            finalText += "You won! Congratulations!!"
            scoreLabel = Label(t, text = finalText, font = labelfont, fg = "Green")
        elif(self.won<self.lost):
            finalText += "You lost. Better luck next time!"
            scoreLabel = Label(t, text = finalText, font = labelfont, fg = "Red")
        else:
            finalText += "You broke even!"
            scoreLabel = Label(t, text = finalText, font = labelfont, fg = "Blue")   
        
        scoreLabel.pack(padx = 20, pady = 20)
        exitButton = Button(text="Exit", command=exit)
        exitButton.pack(side = RIGHT,padx = 5, pady = 5)
        saveButton = Button(text="Save and Exit", command=saveGame)
        saveButton.pack(side = RIGHT)

        # Position the window to the center of screen 
        centerWindow()

        t.mainloop()
