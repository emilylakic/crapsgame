from tkinter import *

class DisplayPanel:
    
    def __init__(self):
        self.won = 0
        self.lost = 0
        self.point = 0
        
        self.t = Tk()
        self.t.wm_title("Let's Play!")
        self.frame = Frame(self.t,bg="green",height=400,width=400)
        self.frame.pack()

        self.wonLabel = Label(self.t,text="Won:  \n"+str(self.won))
        self.wonLabel.pack(side=LEFT)
        
        self.lostLabel = Label(self.t,text="Lost:  \n"+str(self.lost))
        self.lostLabel.pack(side=RIGHT)

        self.pointLabel = Label(self.t,text="Point:  \n" +str(self.point))
        self.pointLabel.pack(side=BOTTOM)
        self.t.mainloop()

    def update(self,result,point):
        if(result>0):
            self.won+=1
            self.point=0
            self.wonLabel.config(text="Won:  \n"+str(self.won))
        elif(result<0):
            self.lost+=1
            self.point=0
        else:
            self.point=point

        


def main():
    display = DisplayPanel()
    display.update(1,0)

main()
