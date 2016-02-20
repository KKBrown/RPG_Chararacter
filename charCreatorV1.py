# RPG Character Creator Version 1
# Based on and expanded from Charles Wade's original code from August of 2013
# Edits by Kelroy Brown - KelroyBrown.com - February 2016
# Learning and Experimenting with Python by doing fun mini projects

# import statements

import pickle

# initialize variables

choice = None  # menu choices
chars = {}  # dictionary for characters

# constants or global variables

POOL = 30

# do the deed

while choice != "0":

    print("""
    Character Creator
    =================
    Originally written by Charles Wade in August of 2013
    Modified and expanded upon as a learning project by Kelroy Brown (KelroyBrown.com) in February 2016

    Please choose a number corresponding with a menu option below:

    0 - Quit Character Creator
    1 - Create New Character
    2 - Edit Attributes of Existing Character
    3 - Delete Character
    4 - List All Characters
    5 - Save All Characters
    6 - Load All Characters
    7 - Erase All Characters
    """)

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye. Thank you for using the Character Creator")

    # create new char
    elif choice == "1":
        pool = POOL  # get value from constant/global variable
        name = input("What name do you want your character to have?: ")
        while name == "":  # Check if name blank
            name = input("What name do you want your character to have?: ")
        cname = name.capitalize()
        if cname not in chars:  # Check if name unique
            print("\nYou have ", pool, " points to spend on Vitality, Strength, Dexterity, Intelligence, "
                                       "Luck and Wisdom!")
            # Vitality
            vit = input("How much Vitality do you want them to have?: ")
            try:  # error handling
                cvit = int(vit)
            except ValueError:
                print("\nThat is not a number, made Vitality 0 and moving on! You can edit after if it was a mistake.")
                cvit = 0
            while cvit > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cvit = int(input("How much Vitality do you want them to have?: "))
            else:
                pool -= cvit
            print("\nYou have ", pool, " points to spend!")
            # Strength
            strn = input("How much Strength do you want them to have?: ")
            try:
                cstr = int(strn)
            except ValueError:
                print("\nThat is not a number, made Strength 0 and moving on! You can edit after if it was a mistake.")
                cstr = 0
            while cstr > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cstr = int(input("How much Strength do you want them to have?: "))
            else:
                pool -= cstr
            print("\nYou have ", pool, " points to spend!")
            # Dexterity
            dex = input("How much Dexterity do you want them to have?: ")
            try:
                cdex = int(dex)
            except ValueError:
                print("\nThat is not a number, made Dexterity 0 and moving on! You can edit after if it was a mistake"
                      ".")
                cdex = 0
            while cdex > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cdex = int(input("How much Dexterity do you want them to have?: "))
            else:
                pool -= cdex
            print("\nYou have ", pool, " points to spend!")
            # Intelligence
            inteli = input("How much Intelligence do you want them to have?: ")
            try:
                cinteli = int(inteli)
            except ValueError:
                print("\nThat is not a number, making Intelligence 0 and moving on! You can edit after if it was a "
                      "mistake.")
                cinteli = 0
            while cinteli > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cinteli = int(input("How much Intelligence do you want them to have?: "))
            else:
                pool -= cinteli
            print("\nYou have ", pool, " points to spend!")
            # Luck
            luck = input("How much Luck do you want them to have?: ")
            try:
                cluck = int(luck)
            except ValueError:
                print("\nThat is not a number, making Luck 0 and moving on! You can edit after if it was a mistake.")
                cluck = 0
            while cluck > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cluck = int(input("How much Luck do you want them to have?: "))
            else:
                pool -= cluck
            print("\nYou have ", pool, " points to spend!")
            # Spirit
            spir = input("How much Spirit do you want them to have?: ")
            try:
                cspir = int(spir)
            except ValueError:
                print("\nThat is not a number, making Spirit 0 and moving on! You can edit after if it was a mistake.")
                cspir = 0
            while cspir > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cspir = int(input("How much Spirit do you want them to have?: "))
            else:
                pool -= cspir
            print("\nYou have ", pool, " points to spend!")
            # Wisdom
            wis = input("How much wisdom do you want them to have?: ")
            try:
                cwis = int(wis)
            except ValueError:
                print("\nThat is not a number, making wisdom 0 and moving on! You can edit after if it was a mistake.")
                cwis = 0
            while cwis > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cwis = int(input("How much wisdom do you want them to have?: "))
            else:
                pool -= cwis
            # Generating secondary stats - formulae can be editted for each stat as needed
            hp = cvit * cstr
            eva = cdex * cluck
            pDef = cstr * cvit
            mDef = cspir * cwis
            pAtt = cstr * cdex
            mAtt = cinteli * cwis
            spd = cvit * cdex
            mana = cspir * cinteli

            cdic = {"Vitality": cvit, "Strength": cstr, "Dexterity": cdex, "Intelligence": cinteli, "Luck": cluck,
                    "Spirit": cspir, "Wisdom": cwis, "Health": hp, "Evasion": eva, "Physical Defence": pDef,
                    "Magic Defence": mDef, "Physical Attack": pAtt, "Magic Attack": mAtt, "Speed": spd, "Mana": mana }
            chars.update({cname: cdic})
            print("**************************************************\n")
            print("Name: ", cname)
            print("")
            print("Primary Stats")
            print("Vitality: ", cvit)
            print("Strength: ", cstr)
            print("Dexterity: ", cdex)
            print("Intelligence: ", cinteli)
            print("Luck: ", cluck)
            print("Spirit: ", cspir)
            print("Wisdom: ", cwis)
            print("")
            print("Secondary Stats")
            print("Health: ", hp)
            print("Evasion: ", eva)
            print("Physical Defence: ", pDef)
            print("Magic Defence: ", mDef)
            print("Physical Attack: ", pAtt)
            print("Magic Attack: ", mAtt)
            print("Speed: ", spd)
            print("Mana: ", mana)
            print("**************************************************\n")
        else:
            print("\nCharacter already exsists! Try editing it or deleting it!")

    # edit chars
    elif choice == "2":
        print("\nHere are all of your characters you can currently edit:\n")
        for key in chars:
            print(key)
        editchar = input("Which character would you like to edit?: ")
        editcharCap = editchar.capitalize()
        if editcharCap in chars:
            pool2 = POOL
            print("\nYou have ", pool2, " points to spend on Vitality, Strength, Dexterity, Intelligence, "
                                       "Luck and Wisdom!")
            # Vitality
            vit2 = input("How much Vitality do you want them to have?: ")
            try:
                cvit2 = int(vit2)
            except ValueError:
                print("\nThat is not a number, made Vitality 0 and moving on! You can edit after if it was a mistake.")
                cvit2 = 0
            while cvit2 > pool2:
                print("Not enough points left in pool, you have ", pool2, " points available, try again!")
                cvit2 = int(input("How much Vitality do you want them to have?: "))
            else:
                pool2 -= cvit2
            print("\nYou have ", pool2, " points to spend!")
            # Strength
            strn2 = input("How much Strength do you want them to have?: ")
            try:
                cstr2 = int(strn2)
            except ValueError:
                print("\nThat is not a number, made Strength 0 and moving on! You can edit after if it was a mistake.")
                cstr2 = 0
            while cstr2 > pool2:
                print("Not enough points left in pool, you have ", pool2, " points available, try again!")
                cstr2 = int(input("How much Strength do you want them to have?: "))
            else:
                pool2 -= cstr2
            print("\nYou have ", pool2, " points to spend!")
            # Dexterity
            dex2 = input("How much Dexterity do you want them to have?: ")
            try:
                cdex2 = int(dex2)
            except ValueError:
                print("\nThat is not a number, made Dexterity 0 and moving on! You can edit after if it was a mistake"
                      ".")
                cdex2 = 0
            while cdex2 > pool2:
                print("Not enough points left in pool, you have ", pool2, " points available, try again!")
                cdex2 = int(input("How much Dexterity do you want them to have?: "))
            else:
                pool2 -= cdex2
            print("\nYou have ", pool2, " points to spend!")
            # Intelligence
            inteli2 = input("How much Intelligence do you want them to have?: ")
            try:
                cinteli2 = int(inteli2)
            except ValueError:
                print("\nThat is not a number, making Intelligence 0 and moving on! You can edit after if it was a "
                      "mistake.")
                cinteli2 = 0
            while cinteli2 > pool2:
                print("Not enough points left in pool, you have ", pool2, " points available, try again!")
                cinteli = int(input("How much Intelligence do you want them to have?: "))
            else:
                pool2 -= cinteli2
            print("\nYou have ", pool2, " points to spend!")
            # Luck
            luck2 = input("How much Luck do you want them to have?: ")
            try:
                cluck2 = int(luck2)
            except ValueError:
                print("\nThat is not a number, making Luck 0 and moving on! You can edit after if it was a mistake.")
                cluck2 = 0
            while cluck2 > pool2:
                print("Not enough points left in pool, you have ", pool2, " points available, try again!")
                cluck2 = int(input("How much Luck do you want them to have?: "))
            else:
                pool2 -= cluck2
            print("\nYou have ", pool2, " points to spend!")
            # Spirit
            spir2 = input("How much Spirit do you want them to have?: ")
            try:
                cspir2 = int(spir2)
            except ValueError:
                print("\nThat is not a number, making Spirit 0 and moving on! You can edit after if it was a mistake.")
                cspir2 = 0
            while cspir2 > pool2:
                print("Not enough points left in pool, you have ", pool2, " points available, try again!")
                cspir2 = int(input("How much Spirit do you want them to have?: "))
            else:
                pool2 -= cspir2
            print("\nYou have ", pool2, " points to spend!")
            # Wisdom
            wis2 = input("How much wisdom do you want them to have?: ")
            try:
                cwis2 = int(wis2)
            except ValueError:
                print("\nThat is not a number, making wisdom 0 and moving on! You can edit after if it was a mistake.")
                cwis2 = 0
            while cwis2 > pool2:
                print("Not enough points left in pool, you have ", pool2, " points available, try again!")
                cwis2 = int(input("How much wisdom do you want them to have?: "))
            else:
                pool2 -= cwis2

            # Generating secondary stats - formulae can be editted for each stat as needed
            hp2 = cvit2 * cstr2
            eva2 = cdex2 * cluck2
            pDef2 = cstr2 * cvit2
            mDef2 = cspir2 * cwis2
            pAtt2 = cstr2 * cdex2
            mAtt2 = cinteli2 * cwis2
            spd2 = cvit2 * cdex2
            mana2 = cspir2 * cinteli2
#
            cdic2 = {"Vitality": cvit2, "Strength": cstr2, "Dexterity": cdex2, "Intelligence": cinteli2, "Luck": cluck2,
                    "Spirit": cspir2, "Wisdom": cwis2, "Health": hp2, "Evasion": eva2, "Physical Defence": pDef2,
                    "Magic Defence": mDef2, "Physical Attack": pAtt2, "Magic Attack": mAtt2, "Speed": spd2,
                     "Mana": mana2 }
            chars.update({editcharCap: cdic2})
            print("**************************************************\n")
            print("Name: ", editcharCap)
            print("")
            print("Primary Stats")
            print("Vitality: ", cvit2)
            print("Strength: ", cstr2)
            print("Dexterity: ", cdex2)
            print("Intelligence: ", cinteli2)
            print("Luck: ", cluck2)
            print("Spirit: ", cspir2)
            print("Wisdom: ", cwis2)
            print("")
            print("Secondary Stats")
            print("Health: ", hp2)
            print("Evasion: ", eva2)
            print("Physical Defence: ", pDef2)
            print("Magic Defence: ", mDef2)
            print("Physical Attack: ", pAtt2)
            print("Magic Attack: ", mAtt2)
            print("Speed: ", spd2)
            print("Mana: ", mana2)
            print("**************************************************\n")
        else:
            print("\nThat character doesnt exist, try creating them!")

    # del char
    elif choice == "3":
        chardel = input("Which character would you like to delete?: ")
        chardelCap = chardel.capitalize()
        if chardelCap in chars:
            areusure = input("\nAre you sure you want to delete this character? 'Y' for YES, 'N' for NO: ")
            areusureCap = areusure.upper()
            if areusureCap == "Y":
                del chars[chardelCap]
                print("\nCharacter WAS deleted!")
            else:
                print("\nCharacter NOT deleted!")
        else:
            print("\nThat character doesnt exist!  Try adding it.")

    # list chars
    elif choice == "4":
        if chars:
            for key in chars:
                print(key)
                print(chars.get(key))
        else:
            print("\nYou have no characters! Try creating some!")

    # save chars
    elif choice == "5":
        pickle.dump(chars, open("save.p", "wb"))
        print("\nAll your characters have been saved! Choose option 6 to reload them on next launch!")

    # load chars
    elif choice == "6":
        chars = pickle.load(open("save.p", "rb"))
        print("\nAll the following characters have been loaded from your last save:\n")
        if chars:
            for key in chars:
                print(key)
                print(chars.get(key))
        else:
            print("\nYou have no characters! Try creating some!")

    # wipe all chars
    elif choice == "7":
        areusure2 = input("\nAre you sure you want to erase ALL characters? 'Y' for YES, 'N' for NO: ")
        areusureCap2 = areusure2.upper()
        if areusureCap2 == "Y":
            chars = {}
            print("\nAll characters have been erased!")
        else:
            print("\nCharacters NOT erased!")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
