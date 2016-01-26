# rev 0.01 alpha
# Python Build 3.5.1
# Author: Thomas Calhoun    john.fullmetaljacket@gmail.com

from tkinter import *
import tkinter.messagebox as tkmb

root = Tk()
root.geometry("500x200")

TotalRows = StringVar()
TotalRepeats = StringVar()

CurRows = 0
CurRepeats = 0

def TotalRowsWritten(*args):
    print("TotalRowsWritten",TotalRows.get())
def TotalRepeatsWritten(*args):
    print("TotalRepeatsWritten",TotalRepeats.get())

TotalRowComp = TotalRows
TotalRepeatComp = TotalRepeats

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.mainWindow()

    def mainWindow(self):
        self.master.title("Knit Companion")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Exit", command=self.quit)
        quitButton.place(x=0, y=80)
        TotalRowE = Entry(root, width=4, textvariable=TotalRows)
        TotalRowE.place(x=195, y=25)
        TotalRepeatE = Entry(root, width=4, textvariable=TotalRepeats)
        TotalRepeatE.place(x=195, y=50)
        TotRowLab = Label(self, text='Please enter the total # of Rows')
        TotRowLab.place(x=0, y=25)
        TotRptLab = Label(self, text='Please enter the total # of Repeats')
        TotRptLab.place(x=0, y=50)
        TotRowPrint = Label(root, fg="red", textvariable=TotalRows)
        TotRowPrint.place(x=340, y=25)
        TotRptPrint = Label(root, fg="red", textvariable=TotalRepeats)
        TotRptPrint.place(x=340, y=50)
        ofRowsLab = Label(self, text='of        Total Rows')
        ofRowsLab.place(x=320, y=25)
        ofRptLab = Label(self, text='of        Total Repeats')
        ofRptLab.place(x=320, y=50)
        global mButton1
        mButton1 = Button(text = CurRows, command = aClick, fg = "black", bg = "white")
        mButton1.place(x=280, y=22)
        global mButton2
        mButton2 = Button(text = CurRepeats, command = bClick, fg = "black", bg = "white")
        mButton2.place(x=280, y=48)

def aClick():
    global CurRows
    CurRows += 1
    mButton1.config(text = CurRows)
def bClick():
    global CurRepeats
    CurRepeats += 1
    mButton2.config(text = CurRepeats)

TotalRows.trace("w", TotalRowsWritten)
TotalRepeats.trace("w", TotalRepeatsWritten)

#TODO: fix conditional error from StrVar() variables above to INT or reconfigure
#TODO> the variable entry altogether. Remaining code deactivated until fixed.
#TODO: bind keystroke <space> as conditional for "if" statement.
#while CurRepeats < TotalRepeatComp:
#    if aClick():
#        CurRows += 1
#    if CurRows == TotalRowComp:
#        CurRepeats += 1
#        CurRows = 0
#        if CurRepeats == TotalRepeatComp:
#                if tkmb.askokcancel(title="Close App", message="Pattern Complete\nWould you like to exit?"):
#                    root.destroy()

app = Window(root)
root.mainloop()