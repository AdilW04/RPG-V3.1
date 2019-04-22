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
import music
import battle
import sys
from time import sleep

names=["Perilous Plains","Dusty Dunes","Mythril","Rustic Ruins"]
monsters=[[RAGING_ROACH,ANGRY_ALBATROSS,SERIOUS_SASQUATCH,CRUMBLIN_CANNON],[ANGRY_ALBATROSS,CRUMBLIN_CANNON],[ANGRY_ALBATROSS,CRUMBLIN_CANNON,SERIOUS_SASQUATCH],[BASALISK]]#RAGING_ROACH,SERIOUS_SASQUATCH,ANGRY_ALBATROSS
unlockableWeapons=[[ANCIENT_BOW,MOSSY_WARHAMMER],[ANCIENT_BOW,MOSSY_WARHAMMER,RUSTY_SWORD],[ANCIENT_BOW,MOSSY_WARHAMMER,RUSTY_SWORD],[ANCIENT_BOW,MOSSY_WARHAMMER,RUSTY_SWORD]]
distances=[23,28,32,36]#distance to end of level
encounterChances=[[85,65],[87,67],[90,70],[94,74]]#more added as levels get added
#                 dig/map
availableTechs=[[ENHANCE,INFERNIX],[ENHANCE,CHILLIX,INFERNIX],[ENHANCE,CHILLIX,HURRIX,INFERNIX],[ENHANCE,INFERNIX,HURRIX,CHILLIX]]
difficulty=[[[1,2],[0,1]],[[1,3],[0,2]],[[2,4],[1,2]],[[3,5],[2,4]]]
themes=["perilous_plains.mp3","perilous_plains.mp3","perilous_plains.mp3","shop.mp3"]
battleThemes=["battle_a.mp3","battle_b.mp3","battle_b.mp3","battle_c.mp3"]

class level:
    def __init__(self,i):
        self.name=names[i]
        self.monsters=monsters[i]
        self.weapons=unlockableWeapons[i]
        self.distance=distances[i]
        self.encounterChances=encounterChances[i]
        self.availableTechs=availableTechs[i]
        self.difficulty=difficulty[i]
        self.theme=themes[i]
        self.battleTheme=battleThemes[i]
    def start(self,player):
        music.Music(PLAY,self.theme,-1)
        write("You are now in {}{}".format(BOLD+ORANGE+NONEB,self.name))
        write("You are {}{} KM{} away from the next portal".format(BOLD+ORANGE+NONEB,self.distance,NORMAL))
        unrecognised.loop=True
        while unrecognised.loop==True:
            unrecognised.loop=False
            print()
            print("{}HP: {}   MP: {}   AR: {}   WP: {}   YEILD: {}{}".format(ITALICS+WHITE+NONEB,player.hp,player.mp,player.armour.name,player.weapon.name,player.money,NORMAL))
            command=input("<1>Dig For Treasure/<2>Advance Forward/<3>Save and Exit↓ \n")
            command=command.upper()
            commands={
                "1":self.dig,
                "2":self.forward,
                "3":pickle.dump
            }
            f=open(player.name+RPG,"wb")
            if command=="4":
                loading.Loading_animation(6,"Good Bye {}!                        ".format(player.name),"SAVING Please Wait")
            commands.get(command,unrecognised.Invalid)(player,f)
    def forward(self,player,*args):
        write("{} moves forward along the trail....".format (player.name))
        for i in range (0):
            sys.stdout.write(".")
            sys.stdout.flush()
            sleep(0.5)
            sys.stdout.write(".")
            sys.stdout.flush()
            sleep(0.5)
            sys.stdout.write(".")
            sys.stdout.flush()
            sleep(0.5)
        encounterRNG=random.randint(1,100)
        if encounterRNG<=self.encounterChances[1]:
            monster=self.Create_monster(player,self.difficulty[1])
            battle.Battle(player,player.opponent)
        else:
            write("The course was clear!")
        self.distance=self.distance-random.randint(4,20)
        self.start(player)


    def dig(self,player,*args):
        encounterRNG=random.randint(1,100)
        write("\n{} digs for treasure...".format(player.name))
        for i in range (0):
            sys.stdout.write(".")
            sys.stdout.flush()
            sleep(0.5)
            sys.stdout.write(".")
            sys.stdout.flush()
            sleep(0.5)
            sys.stdout.write(".")
            sys.stdout.flush()
            sleep(0.5)
        if encounterRNG<=self.encounterChances[0]:
            monster=self.Create_monster(player,self.difficulty[0])
            battle.Battle(player,player.opponent)
        else:
            write("  No enemies in sight!")
        self.start(player)
        


    def Create_monster(self,player,difficulty):
        monstersProperties=[]
        techAmount=random.randint(difficulty[0],difficulty[1])
        check=0
        hpBonus=techAmount*8
        atkBonus=round(techAmount*3.4)
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
        player.opponent.hp+=hpBonus
        player.opponent.ATK+=atkBonus


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
        write("  OH NO")
        write("{}{}{}{}{} appears!".format (ana,NONE+RED+NONEB,desc,monster.name,NORMAL))
        return(monster)
       
perilousPlains=level(PERILOUS_PLAINS)
dustyDunes=level(DUSTY_DUNES)
mythril=level(MYTHRIL)
rusticRuins=level(RUSTIC_RUINS)


