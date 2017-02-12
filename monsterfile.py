import os

print ("Do you want to see the list of monsters?")
seemonsters = raw_input("Y / N : ");
seemonsters = seemonsters.lower()
if (seemonsters == "y"):
    monsterfile = open("monsters.txt", "r+")
    monsterlist = monsterfile.readlines();
    for i in range(len(monsterlist)):
        print monsterlist[i]
    print("\nDo yo want to add a monster?")
    addmonster = raw_input("Y / N : ");
    addmonster = addmonster.lower()
    if (addmonster == "y"):
        newmonster = raw_input("Enter the name of your monster: ");
        newmonster = newmonster + "\n"
        monsterfile.write(newmonster);
    else:
        print("Too scared?")
    monsterfile.close();
else:
    print("CHICKEN!!!")
