# rev 0.01 alpha
# Python Build 3.5.1
# Author: Thomas Calhoun    john.fullmetaljacket@gmail.com

print('''
>Welcome to "TheDisturbed50\'s Knit Companion"!
>You are in the Command-Prompt edition, ver. 0.02alpha
>Please follow the prompts and bear with me on the user
   input requirements as I work on possible workarounds.
   Thank you!
      ~Thomas Calhoun \n
''')
print("        ***Patern Input***")
print('''Please note: if your pattern increases rows,
 break down the input into "Phases" as you complete it.\n''')
TotalRows = int(input("Enter the total number of rows     -->"))
TotalRepeats = int(input("Enter the total number of repeats  -->"))
CurRows = 0
CurRepeats = 0

while CurRepeats < TotalRepeats:
    print("...Currently %d of %d Rows" % (CurRows,TotalRows))
    print("...Currently %d of %d Repeats" % (CurRepeats,TotalRepeats))
    if int(input("Enter any number, then press Enter for Row Complete...\n")) < 10:
        CurRows += 1
        if CurRows == TotalRows:
            CurRepeats += 1
<<<<<<< HEAD
            CurRows = 0
            print(">>>Good Work! Next Row!\n\n")
            if CurRepeats == TotalRepeats:
                print("/n/n~*/Good Job! Pattern Complete!\\*~")
				input("Press enter to exit...")
            else:
                continue
        else:
            continue
    else:
        continue
=======
            mButton2.config(text = CurRepeats)
        mButton1 = Button(text = CurRows, command = aClick, fg = "black", bg = "white")
        mButton1.place(x=280, y=22)
        mButton2 = Button(text = CurRepeats, command = bClick, fg = "black", bg = "white")
        mButton2.place(x=280, y=48)

app = Window(root)
root.mainloop()
>>>>>>> origin/master
