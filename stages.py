import players
from constants import *
from write_text import write
import unrecognised
import random
import enemies
import omega_arts
import weapons
import armour
import win_lose
import pickle
import loading
import threading

names=["Perilous Plains","Dusty Dunes","Velen","Spagonia Ruins"]
monsters=[[RAGING_ROACH,ANGRY_ALBATROSS]]#RAGING_ROACH,SERIOUS_SASQUATCH,ANGRY_ALBATROSS
unlockableWeapons=[[ANCIENT_BOW,MOSSY_WARHAMMER,RUSTY_SWORD]]
distances=[43,54,68,72]#distance to end of level
encounterChances=[[100,69]]#more added as levels get added
#                 dig/map
availableTechs=[[HURRIX]]
difficulty=[[0,2],[1,3],[2,4],[3,5]]
class level:
    def __init__(self,i):
        self.name=names[i]
        self.monsters=monsters[i]
        self.weapons=unlockableWeapons[i]
        self.distance=distances[i]
        self.encounterChances=encounterChances[i]
        self.availableTechs=availableTechs[i]
        self.difficulty=difficulty[i]
    def start(self,player):
        player.weapon=weapons.weapon(DULL_DAGGER,player)
        player.armour=armour.armour(BIKER_JACKET)
        write("You are now in {}{}".format(BOLD+ORANGE+NONEB,self.name))
        write("You are {}{} KM{} away from the next portal".format(BOLD+ORANGE+NONEB,self.distance,NORMAL))
        write()
        unrecognised.loop=True
        while unrecognised.loop==True:
            unrecognised.loop=False
            print("{}HP: {}   MP: {}   AR: {}   WP: {}   YEILD: {}{}".format(ITALICS+WHITE+NONEB,player.hp,player.mp,player.armour.name,player.weapon.name,player.money,NORMAL))
            command=input("☾ ⋆* [1]Dig For Treasure/[2]Advance Forward/[3]Inventory/[4]Save and Exit⋆*･ﾟ: ")
            command=command.upper()
            commands={
                "1":self.dig,
                "4":pickle.dump
            }
            f=open(player.name+RPG,"wb")
            if command=="4":
                loading.Loading_animation(6,"Good Bye {}!                        ".format(player.name),"SAVING Please Wait")
            commands.get(command,unrecognised.Invalid)(player,f)
    def dig(self,player,*args):
        encounterRNG=random.randint(1,100)
        write("\n{} digs for treasure...".format(player.name))
        if encounterRNG<=self.encounterChances[0]:
            monster=self.Create_monster(player)
        #test
        loop=True
        player.activeEffects.clear()
        player.isFrozen=False
        player.isEnhanced=False
        while loop==True:
            player.Action()
            loop=win_lose.Win_lose(player)
            if loop==False:
                break
            player.opponent.Enemy_turn()
            loop=win_lose.Win_lose(player)
        self.start(player)
        


    def Create_monster(self,player):
        monstersProperties=[]
        techAmount=random.randint(self.difficulty[0],self.difficulty[1])
        check=0
        for item in self.availableTechs:
            check=check+1
        if techAmount>check:
            techAmount=check
        for i in range (techAmount):
            while True:
                choice=random.choice(self.availableTechs)
                if choice not in monstersProperties:
                    monstersProperties.append(choice)
                    break

                
        for tech in monstersProperties:
            techIndex=monstersProperties.index(tech)#create magic obj and assign it to enemy list
            monstersProperties[techIndex]=omega_arts.magic(tech,player)
        monsterSpecies=random.choice(self.monsters)
        monster=enemies.enemy(monsterSpecies,player,monstersProperties)
        player.opponent=monster

        desc=""
        #dscription of monster (magic properties)
        ana=""#an or a
        try:
            if monstersProperties[0].monsterProperty[0]=="A" or monstersProperties[0].monsterProperty[0]=="E"or monstersProperties[0].monsterProperty[0]=="I"or monstersProperties[0].monsterProperty[0]=="O"or monstersProperties[0].monsterProperty[0]=="U":
                ana="An "
            else:
                ana="A "
        except AttributeError:
            pass
        for tech in monstersProperties:#property of tech used for monster
            if isinstance(tech,omega_arts.magic):
                desc=desc+tech.monsterProperty
                desc=desc+", "
        write("OH NO")
        write("{}{}{}{}{} appears!".format (ana,NONE+RED+NONEB,desc,monster.name,NORMAL))
        return(monster)
       


