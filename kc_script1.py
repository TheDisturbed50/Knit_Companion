# rev 0.1 alpha
# Python Build 3.5.1
# Author: Thomas Calhoun    john.fullmetaljacket@gmail.com

#!/usr/bin/env python
import sys
import math
from tkinter import *

root = Tk()
root.geometry("600x200")

TotalRows = StringVar()
TotalRepeats = StringVar()

global CurRows
CurRows = 0
global CurRepeats
CurRepeats = 0

def TotalRowsWritten(*args):
    print("TotalRowsWritten",TotalRows.get())
def TotalRepeatsWritten(*args):
    print("TotalRepeatsWritten",TotalRepeats.get())

TotalRows.trace("w", TotalRowsWritten)
TotalRepeats.trace("w", TotalRepeatsWritten)

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
        TotRowLab = Label(self, text='Please enter the total # of Rows')
        TotRowLab.place(x=0, y=25)
        TotRptLab = Label(self, text='Please enter the total # of Repeats')
        TotRptLab.place(x=0, y=50)
        TotRowEnt = Entry(root, width=4, textvariable=TotalRows)
        TotRowEnt.place(x=195, y=25)
        TotRptEnt = Entry(root, width=4, textvariable=TotalRepeats)
        TotRptEnt.place(x=195, y=50)
        TotRowPrint = Label(root, fg="red", textvariable=TotalRows)
        TotRowPrint.place(x=340, y=25)
        TotRptPrint = Label(root, fg="red", textvariable=TotalRepeats)
        TotRptPrint.place(x=340, y=50)
        ofRowsLab = Label(self, text='of        Total Rows')
        ofRowsLab.place(x=320, y=25)
        ofRptLab = Label(self, text='of        Total Repeats')
        ofRptLab.place(x=320, y=50)
        def aClick():
            global CurRows
            CurRows += 1
            mButton1.config(text = CurRows)
        def bClick():
            global CurRepeats
            CurRepeats += 1
            mButton2.config(text = CurRepeats)
        mButton1 = Button(text = CurRows, command = aClick, fg = "black", bg = "white")
        mButton1.place(x=280, y=22)
        mButton2 = Button(text = CurRepeats, command = bClick, fg = "black", bg = "white")
        mButton2.place(x=280, y=48)

app = Window(root)
root.mainloop()