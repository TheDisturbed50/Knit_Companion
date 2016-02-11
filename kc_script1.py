# rev 0.1 beta
# Python Build 3.5.1
# Author: Thomas Calhoun    john.fullmetaljacket@gmail.com

print('''Welcome to "TheDisturbed50\'s Knit Companion"!

You are in the Command-Prompt edition, ver. 0.1beta

Please follow the prompts, from there it is as simple as
pressing "Enter" for each completed row.

   Enjoy!
      ~Thomas Calhoun \n\n''')

print("        ***Pattern Input***\n")
print('''Please note: if your pattern increases rows,
 break down the input into "Phases" as you complete it.\n''')
TotalRows = int(input("Enter the total number of rows     -->"))
TotalRepeats = int(input("Enter the total number of repeats  -->"))
CurRows = 0
CurRepeats = 0
TotalRowComp = TotalRows+1
TotalRepeatComp = TotalRepeats+1

while CurRepeats < TotalRepeatComp:
    print("...Currently %d of %d Rows" % (CurRows,TotalRows))
    print("...Currently %d of %d Repeats\n" % (CurRepeats,TotalRepeats))
    if input("Press Enter for Row Complete...\n") in [""]:
        CurRows += 1
        if CurRows == TotalRowComp:
            CurRepeats += 1
            CurRows = 0
            print("   Good Work! Next Row!\n\n")
            if CurRepeats == TotalRepeatComp:
                print("\n\n   Excellent! Pattern Complete!")
                input("Press enter to exit...")
            else:
                continue
        else:
            continue
    else:
        continue
