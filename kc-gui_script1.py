# rev 0.02 alpha
# Python Build 3.5.1
# Author: Thomas Calhoun    john.fullmetaljacket@gmail.com

from tkinter import *
import tkinter.messagebox as tkmb

root = Tk()
root.geometry("500x200")
root.title("Knit Companion")

ttlRow = IntVar()
ttlRpt = IntVar()
scRow = IntVar()
scRow.set(0)
scRpt = IntVar()
scRpt.set(0)

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
    def exitPrompt(): #Messagebox verify to exit (from buttons)
        if tkmb.askokcancel(title="Close App", message="Please verify,\nWould you like to exit?"):
            root.destroy()

    quitButton = Button(root, text="Exit", command=exitPrompt)
    quitButton.place(x=0, y=80)
    TotalRowEntry = Entry(root, width=4, textvariable=ttlRow)
    TotalRowEntry.place(x=195, y=25)
    TotalRepeatEntry = Entry(root, width=4, textvariable=ttlRpt)
    TotalRepeatEntry.place(x=195, y=50)
    setCurRow = Entry(root, width=4, fg="black", textvariable=scRow)
    setCurRow.place(x=240, y=25)
    setCurRpt = Entry(root, width=4, fg="black", textvariable=scRpt)
    setCurRpt.place(x=240, y=50)
    TotRowLab = Label(root, text='Please enter the total # of Rows')
    TotRowLab.place(x=0, y=25)
    TotRptLab = Label(root, text='Please enter the total # of Repeats')
    TotRptLab.place(x=0, y=50)
    ofRowsLab = Label(root, text='of        Total Rows')
    ofRowsLab.place(x=320, y=25)
    ofRptLab = Label(root, text='of        Total Repeats')
    ofRptLab.place(x=320, y=50)
    TotRowPrint = Label(root, fg="red", textvariable=ttlRow)
    TotRowPrint.place(x=340, y=25)
    TotRptPrint = Label(root, fg="red", textvariable=ttlRpt)
    TotRptPrint.place(x=340, y=50)
    curRowPrint = Label(root, fg="red", textvariable=scRow)
    curRowPrint.place(x=300, y=25)
    curRptPrint = Label(root, fg="red", textvariable=scRpt)
    curRptPrint.place(x=300, y=50)
    setLabel = Label(root, fg='blue', text='(SET)')
    setLabel.place(x=233, y=0)
    def run(root):
        root.mainloop()
    TotalRows = int(ttlRow.get())
    TotalRepeats = int(ttlRpt.get())
    CurRows = int(scRow.get())
    CurRepeats = int(scRpt.get())
    def traceCallback(*args):
        print("traceCallback")
    ttlRow.trace("w", traceCallback)
    ttlRpt.trace("w", traceCallback)
    scRow.trace("w", traceCallback)
    scRpt.trace("w", traceCallback)
    def rowIteration(self):
        if self.TotalRepeats > self.CurRepeats:
            if self.TotalRows < self.CurRows:
                self.CurRepeats += 1
                scRow.set(0)
                if self.TotalRepeats < self.CurRepeats:
                    if tkmb.askokcancel(title="Close App", message="Pattern Complete\nWould you like to exit?"):
                        root.destroy()
    def readyClick(*args): #STILL BROKEN
        CurRows += 1 #BRK
        rowIteration() #BRK
    click = readyClick
    readyButton = Button(text=CurRows, command=click, fg='black')
    readyButton.place(x=180, y=100)
    readySpace = Entry(text="Click here to begin")
    readySpace.place(x=180, y=130)

root.bind("<space>", App.click)

app = App(root)
app.run()
root.mainloop()