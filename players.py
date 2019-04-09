import login
import enemies
import weapons
from unrecognised import Invalid
from write_text import write
import defend
import omega_arts
from constants import *
import armour
import stages
stages=[stages.perilousPlains,stages.dustyDunes,stages.mythril,stages.rusticRuins]
#have a level class later

class Player:

    def __init__(self,mp,hp):#remember that the player also has what omega arts he has as an atribute
        global perilousPlains
        global white
        self.mp=mp
        self.hp=hp
        self.name=login.Get_heroName()
        self.createObj=True
        self.guard=defend.defendClass(self)
        self.omegaArts=omega_arts.omegaArts(self)
        self.opponent=None
        self.weapon=None
        self.armour=None
        self.activeEffects=[]
        self.isEnhanced=False
        self.stage=None
        #perilousPlains = stages.level(PERILOUS_PLAINS)
        self.stageNo=3
        self.stage=stages[self.stageNo]
        self.color="\033[0;37;32m"
        self.isFrozen=False
        self.isDizzy=False
        self.money=0

    def Start_battle(self):
        pass
    
    # def Pass_vals_to_guard(self):
    #   defend.Defend(self)
    #   self.loop=False
    
    def Unlock_OA(self):
        self.omegaArts=omega_arts.omegaArts(self)#also creates omega arts obj for people loading old samves
        #only creates object once
        # try:
        #   if self.omegaArts.techs[0].name=="Enhance":
        #       pass
        #   if self.omegaArts.techs[1].name=="Infernix":
        #       pass
        # except IndexError:#shows that it isnt in the techs list
        #   self.omegaArts.techs.append(enhance)
        #   self.omegaArts.techs.append(infernix)
        #   enemies.enemyTechs.append(infernix)
        self.omegaArts.techs[omega_arts.enhance]=True
        self.omegaArts.techs[omega_arts.infernix]=True
        self.omegaArts.techs[omega_arts.chillix]=True
        self.omegaArts.techs[omega_arts.hurrix]=True



    def Create_main_objs(self):
        pass
        # global enhance
        # global infernix
        # global ragingRoach
        # global seriousSasquatch
        # global ogled
        # global dullDagger
        # global mossyWarhammer
        # global ancientBow
        # global creasedShirt
        # global luckyJumper
        # global bikerJacket
        # global emmanuelUniform
        # global basalisk
        # global perilousPlains
        #ENEMIES
        # ragingRoach=enemies.enemy(RAGING_ROACH,self)
        # seriousSasquatch=enemies.enemy(SERIOUS_SASQUATCH,self)
        # ogled=enemies.enemy(OGLED,self)
        # basalisk=enemies.enemy(BASALISK,self)
        #WEAPONS
        # dullDagger=weapons.weapon(DULL_DAGGER,self)
        # mossyWarhammer=weapons.weapon(MOSSY_WARHAMMER,self)
        # ancientBow=weapons.weapon(ANCIENT_BOW,self)
        #ARMOUR
        # creasedShirt=armour.armour(CREASED_SHIRT)
        # luckyJumper=armour.armour(LUCKY_JUMPER)
        # bikerJacket=armour.armour(BIKER_JACKET)
        # emmanuelUniform=armour.armour(EMMANUEL_UNIFORM)
        #OMEGA ARTS
        # enhance=omega_arts.magic(ENHANCE,self)
        # infernix=omega_arts.magic(INFERNIX,self)
        #STAGES
    def Immobile(self,*args):
        write("{} cant move right now!".format (self.name))
        self.loop=False
    
    def Action(self):  
        if self.weapon.chainCount==0:
                self.weapon.crit=weapons.crit[self.weapon.i]
        if self.guard.isGuarding==True:
            self.guard.Restore()#checks if your guarding
            
        

        #creates the all enemy and weapon objects
        #self.Create_main_objs()

        #print(self.omegaArts.active)
        
        # for active in self.omegaArts.active:
        #     print(active.name,active.effectCounter)
        #-1 to magic effect
        
        # for active in self.omegaArts.active:
        #     if active.effectCounter>0:
        #       active.effectCounter=active.effectCounter-1
        
        #guard
        # print(self.opponent.atk)
        # print(self.opponent.ATK)     

        self.name=login.Get_heroName()
        write("It is "+self.name+"'s turn...")
        for activeEffect in self.activeEffects:
            activeEffect.effectDamage(self)
        self.loop=True
        while self.loop==True:
            effects=""
            for effect in self.activeEffects:
                if effect.techType=="statBuff":
                    effects=effects+DIM+GREEN+NONEB+effect.effectName+NORMAL
                else:
                    effects=effects+NONE+RED+NONEB+effect.effectName+NORMAL

                
                effects=effects+"  "
            if effects=="":
                effects="None"  
            print(self.opponent.mp)      
            print("Effects:",effects)
            oppAbb={
                self.opponent.name:self.opponent.abb
            }#opponent abbreviation
            print("{}MP: {}   HP: {}          {}: {}{}{} ".format(DIM+GREEN+NONEB,self.mp,self.hp,oppAbb.get(self.opponent.name,"???"),DIM+RED+NONEB,self.opponent.hp,NORMAL))
            if self.isFrozen==False and self.isDizzy==False:
                commands=input("☾ ⋆*Attack/Defend/Omega Arts/Items⋆*･ﾟ: ".format(self.color))
                commands=commands.upper()
                command={
                    "ATTACK":self.weapon.Attack_enemy,
                    "DEFEND":self.guard.Guard ,
                    "OMEGA ARTS":self.omegaArts.Omega_arts ,
                    "OMEGA":self.omegaArts.Omega_arts 
                }
                
                a=command.get(commands,Invalid)(self)
            else:
                self.Immobile()

    def Flip(self,**kwargs):#function that allows me to change player variables based on paramaters
        if list(kwargs.keys())[0]=="isEnhanced":
            self.isEnhanced=kwargs.get("isEnhanced")#gets "isDefending" from dicitionsry key and value entered into the brackets when called 
        if list(kwargs.keys())[0]=="isFrozen":
            self.isFrozen=kwargs.get("isFrozen")
        if list(kwargs.keys())[0]=="isDizzy":
            self.isDizzy=kwargs.get("isDizzy")
    def Do_dmg(self,damage):
        if self.isEnhanced==True:
            damage=damage*3
        #might add more stuff that effects damage
        self.opponent.Lose_hp(damage)

    def Lose_hp(self,damage,regAtk,*args):#cause for damage
        #print("isGuarding",self.guard.isGuarding)#ready means ready to attack i know it
        if self.guard.isGuarding==True:# and "effectDmg" not in args:#checks args list to see if the information for when its effect damage is there, can be expanded upon later :D
            damage=round(damage/3)
        if regAtk==True:#reg atk
            damage=(damage-self.armour.reduction)#* (1 - resistance) eventually
        if damage<0:#ensures that you dont get minus hp damage
            damage=0    
        write("{}It did a damage of {}".format (NONE+RED+NONEB,damage))

        if damage==0:
            write("Complete Nulification!")
        self.hp=self.hp-damage

    def Lose_mp(self,playerMpLoss):
        playerMpLoss=(playerMpLoss-self.armour.mp)
        self.mp=self.mp-playerMpLoss
    def Lose_money(self,loss):
        self.money=self.money-loss
    def Add_money(self,gain):
        self.money=self.money+gain
# player1=Player(120,500)#omega arts
#allPlayers=[player1]