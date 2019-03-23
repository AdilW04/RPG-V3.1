from time import sleep
from constants import *
from write_text import write
def Tutorial():
    for char in "This is the tutorial\n":
        WRITE(char)
        sleep(TXT)
    sleep(SLP)
    print()
    print("☾ ⋆*Attack⋆*･ﾟ:")
    print()
    sleep(SLP)
    write("what you see above you is the command bar, type in a command here to follow through with that particular action. Try it now!")
    while True:
        sleep(SLP)
        print()
        command=input("☾ ⋆*Attack⋆*･ﾟ: ")
        command=command.upper()
        print()
        sleep(SLP)
        if command =="ATTACK":
            write("The hero attacks dealing a damage of 10!")
            break
        else:
            for char in "Just type in the command!\n":
                WRITE(char)
                FLUSH()
                sleep(TXT)
    for char in "Good! You attacked the enemy, reducing their hp by 10!\n":
        WRITE(char)
        FLUSH()
        sleep(TXT)
    sleep(SLP)
    write("The enemy's hp is now 40!")
    sleep(SLP)
    for char in "The enemy is about to attack now!\n":
        WRITE(char)
        FLUSH()
        sleep(TXT)
    print()
    sleep(SLP)
    write("It is the enemy's turn now..")
    print()
    sleep(SLP)
    write("The enemy attacks dealing a damage of 8!")
    sleep(SLP)
    for char in "OUCH! that must have hurt! keep in mind that the enemy can do a critical on you!\n":
        WRITE(char)
        FLUSH()
        sleep(TXT)
    for char in ("Your HP is now 492!\n"):
        WRITE(char)
        FLUSH()
        sleep(TXT)

    for char in "Now lets try defending!":
        WRITE(char)
        FLUSH()
        sleep(TXT)
    while True:
        sleep(SLP)
        print()
        command=input("☾ ⋆*Attack/Defend⋆*･ﾟ: ")
        command=command.upper()
        print()
        sleep(SLP)
        if command =="DEFEND":
            write("The hero defends for 1 turn")
            break
        else:
            for char in "Just type in defend!\n":
                WRITE(char)
                FLUSH()
                sleep(TXT)
    for char in "now your guard is up, lets see what happens when the enemy attacks you!\n":
        WRITE(char)
        FLUSH()
        sleep(TXT)
    sleep(SLP)
    print()
    write("It is the enemy's turn now...")
    sleep(SLP)
    print()
    write("The enemy attacks dealing a damage of 1!")
    sleep(SLP)
    write("Your HP is now 491!")
    sleep(SLP)
    for char in "Now you see how useful defend is! but remember you also need to attack in order to win!\n":
        WRITE(char)
        FLUSH()
        sleep(TXT)
    for char in "Now lets try omega arts!\n":
        WRITE(char)
        FLUSH()
        sleep(TXT)
    while True:
        sleep(SLP)
        print()
        sleep(SLP)
        write("Your mp is 40")
        sleep(SLP)
        for char in "This is your Mana, You need it to use omega arts!\n":
            WRITE(char)
            FLUSH()
            sleep(TXT)
        command=input("☾ ⋆*Attack/Defend/Omega arts⋆*･ﾟ: ")
        command=command.upper()
        print()
        sleep(SLP)
        if command =="OMEGA ARTS":
            for art in tutorialArts:
                write("    > "+art)
            for char in "Every omega art requires MP, so if you dont have enough mp you can not use the technique\n":
                WRITE(char)
                FLUSH()
                sleep(TXT)
            for char in "This is The arts panel, type in enhance and see what happens! ":
                WRITE(char)
                FLUSH()
                sleep(TXT)
            while True:
                tech=input()
                tech=tech.upper()
                if tech=="ENHANCE":
                    write("You focus MANA into to your weapon..")
                    sleep(SLP)
                    write("Your attack power has increased for 3 turns!")
                    break
                else:
                    for char in "Just type in enhance!\n":
                        WRITE(char)
                        FLUSH()
                        sleep(TXT)
        else:
            for char in "Just type in omega arts in!\n":
                WRITE(char)
                FLUSH()
                sleep(TXT)
        write("Good!")
        sleep(SLP)
        print()
        write("It is the enemy's turn now...")
        print()
        sleep(SLP)
        for char in "The enemy attacks dealing a damage of 8!\n":
            WRITE(char)
            FLUSH()
            sleep(TXT)
        sleep(SLP)
        write("Your HP is now 483")
        sleep(SLP)
        for char in "Now attack and see what happens!\n":
            WRITE(char)
            FLUSH()
            sleep(TXT)
        write("Your mana is now 0")
        sleep(SLP)
        while True:
            command=input("☾ ⋆*Attack/Defend/Omega arts⋆*･ﾟ: ")
            command=command.upper()
            if command=="ATTACK":
                write("The hero attacks dealing a damage of 25!")
                sleep(SLP)
                break
            else:
                for char in "Just type in attack\n":
                    WRITE(char)
                    FLUSH()
                    sleep(TXT)
        write("The enemy's hp is now 15!")
        for char in "You can also use items like potions to help you in battle\n You will face a variety of opponents the likes of which you have never seen before.\n Use the skills You have learnt and the abilities you will learn to smite your foes!\n":
            WRITE(char)
            FLUSH()
            sleep(TXT)
        sleep(SLP)
        for char in "Good luck out there!\n":
            WRITE(char)
            FLUSH()
            sleep(TXT)
        return()
    
    