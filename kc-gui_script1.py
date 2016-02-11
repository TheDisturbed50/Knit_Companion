# rev 0.02 alpha
# Python Build 3.5.1
# Author: Thomas Calhoun    john.fullmetaljacket@gmail.com

from tkinter import *
import tkinter.messagebox as tkmb

root = Tk()
root.geometry("500x200")
root.title("Knit Companion")

class App(Frame):
    def __init__(root, master):
        Frame.__init__(root, master)
        root.grid()
        #root.create_widgets()

    def exitPrompt(): #Messagebox verify to exit (from buttons)
        if tkmb.askokcancel(title="Close App", message="Please verify,\nWould you like to exit?"):
            root.destroy()

    ttlRow = IntVar()
    ttlRpt = IntVar()
    scRow = IntVar()
    scRow.set(0)
    scRpt = IntVar()
    scRpt.set(0)

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

    TotalRows = int(ttlRow.get())
    TotalRepeats = int(ttlRpt.get())
    CurRows = int(scRow.get())
    CurRepeats = int(scRpt.get())

    def on_trace_choice(self, name, index, mode):
        self.refresh()

    ttlRow.trace("w", on_trace_choice)
    ttlRpt.trace("w", on_trace_choice)
    scRow.trace("w", on_trace_choice)
    scRpt.trace("w", on_trace_choice)

    #TODO >debug the following conditional, it is causing the application to crash at the 'while' loop
    def rowIteration(*args):
        while root.TotalRepeats > root.CurRepeats:
            if root.TotalRows < root.CurRows:
                root.CurRepeats += 1
                root.scRow.set(0)
                if root.TotalRepeats < root.CurRepeats:
                    if tkmb.askokcancel(title="Close App", message="Pattern Complete\nWould you like to exit?"):
                        root.destroy()

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


    def readyClick(*args):
        CurRows += 1
        rowIteration()
        readyButton.config(text=root.CurRows)

    readyButton = Button(text='Click below when ready!', command=readyClick, fg='black')
    readyButton.place(x=180, y=100)
    readySpace = Entry(text="Click here to begin")
    readySpace.place(x=180, y=130)

    def run(root):
        root.mainloop()

    root.bind("<space>", readyClick())

app = App(root)
app.run()
root.mainloop()