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
import inventory
stages=[stages.perilousPlains,stages.dustyDunes,stages.mythril,stages.rusticRuins]

class Player:

    def __init__(self,mp,hp):#remember that the player also has what omega arts he has as an atribute
        global white
        self.mp=mp
        self.hp=hp
        self.maxMp=mp
        self.maxHp=hp
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
        self.stageNo=0
        self.stage=stages[self.stageNo]
        self.color="\033[0;37;32m"
        self.isFrozen=False
        self.isDizzy=False
        self.money=0
        self.coolDown=0
        self.inventory=inventory.items
        self.effects="None"
        self.oppEffects="None"

    def Start_battle(self):
        pass
    
    # def Pass_vals_to_guard(self):
    #   defend.Defend(self)
    #   self.loop=False
    
    def Unlock_OA(self):
        self.omegaArts=omega_arts.omegaArts(self)#also creates omega arts obj for people loading old samves
        self.omegaArts.techs[omega_arts.enhance]=True
        self.omegaArts.techs[omega_arts.infernix]=True
        self.omegaArts.techs[omega_arts.chillix]=True
        self.omegaArts.techs[omega_arts.hurrix]=True



    def Create_main_objs(self):
        pass
    def Immobile(self,*args):
        write("{} cant move right now!".format (self.name))
        self.loop=False
    def Skip(self,*args):
        self.loop=False
    def Stats(self,*args):
        self.Update_effects()
        print("                ~~STATUS OF THE BATTLE~~")
        print("           {}          VS          {}({})".format(self.name,self.opponent.name,self.opponent.abb))
        print("{}'s HEALTH POINTS: {}         {}'s ({}) HEALTH POINTS:{}".format (self.name,self.hp,self.opponent.name,self.opponent.abb,self.opponent.hp if self.opponent.hp>0 else 0))
        print("{}'s MAGIC POINTS: {}          {}'s ({}) STAMINA:{}".format (self.name,self.mp,self.opponent.name,self.opponent.abb,self.opponent.mp))
        print("{}'s CURRENT EFFECTS: {}      {}'s ({}) CURRENT EFFECTS:{}".format(self.name,self.effects,self.opponent.name,self.opponent.abb,self.oppEffects))
        print()
    def Sub_turn(self):
        if self.isFrozen==False and self.isDizzy==False:

            self.loop=True
            while self.loop:
                write("~SubTurn~")

                subCommand=input("--Stats\Items\Skip--")
                subCommand=subCommand.upper()
                commands={
                    "STATS":self.Stats,
                    "ITEMS":self.inventory.Access_in_battle,
                    "SKIP":self.Skip
                }
                a=commands.get(subCommand,Invalid)(self)
    def Update_effects(self):
        effects = ""
        for effect in self.activeEffects:
            if effect.techType == "statBuff":
                effects = effects + DIM + GREEN + NONEB + effect.effectName + NORMAL
            else:
                effects = effects + NONE + RED + NONEB + effect.effectName + NORMAL

            effects = effects + "  "
        if effects == "":
            effects = "None"
        oppEffects = ""
        for effect in self.opponent.activeEffects:
            if effect.techType == "statBuff":
                oppEffects = oppEffects + DIM + RED + NONEB + effect.effectName + NORMAL
            else:
                oppEffects = oppEffects + NONE + GREEN + NONEB + effect.effectName + NORMAL

            oppEffects = oppEffects + "  "
        if oppEffects == "":
            oppEffects = "None"
        self.effects = effects
        self.oppEffects = oppEffects
    def Change_stage(self,stageNo):
        self.stage=stages[stageNo]
    def Action(self):
        if self.coolDown>0:
            self.coolDown=self.coolDown-1
            if self.coolDown==0:
                write("{} can now handle another consumable item!".format (self.name))
        if self.weapon.chainCount==0:
                self.weapon.crit=weapons.crit[self.weapon.i]
        if self.guard.isGuarding==True:
            self.guard.Restore()#checks if your guarding
        
   

        self.name=login.Get_heroName()
        write("It is "+self.name+"'s turn...")
        for activeEffect in self.activeEffects:
            activeEffect.effectDamage(self)
        self.loop=True
        while self.loop==True:
            oppAbb = {
                self.opponent.name: self.opponent.abb
            }  # opponent abbreviation
            self.Update_effects()
            print()
            print("{} Effects:".format(oppAbb.get(self.opponent.name,"???")),self.oppEffects)
            print("Effects:", self.effects)
            print("{}MP: {}   HP: {} |   {}: {}{}   STM: {}{} ".format(DIM+GREEN+NONEB,self.mp,self.hp,oppAbb.get(self.opponent.name,"???"),DIM+RED+NONEB,self.opponent.hp,self.opponent.mp,NORMAL))
            if self.isFrozen==False and self.isDizzy==False:
                commands=input("~~Attack/Defend/Omega Arts¬.: ".format(self.color))
                commands=commands.upper()
                command={
                    "ATTACK":self.weapon.Attack_enemy,
                    "DEFEND":self.guard.Guard ,
                    "OMEGA ARTS":self.omegaArts.Omega_arts ,
                    "OMEGA":self.omegaArts.Omega_arts,
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
            damage=round(damage/4)
        if regAtk==True:#reg atk
            damage=(damage-self.armour.reduction)#* (1 - resistance) eventually
        if damage<0:#ensures that you don't get minus hp damage
            damage=0    
        write("{}It did a damage of {}".format (NONE+RED+NONEB,damage))

        if damage==0:
            write("Complete Nullification!")
        self.hp=self.hp-damage

    def Lose_mp(self,playerMpLoss):
        playerMpLoss=(playerMpLoss-self.armour.mp)
        self.mp=self.mp-playerMpLoss
    def Lose_money(self,loss):
        self.money=self.money-loss
    def Add_money(self,gain):
        self.money=self.money+gain
    def Add_hp(self,hp):
        if self.hp<self.maxHp:
            if (self.hp+hp)>self.maxHp:
                hp=self.maxHp-self.hp
            write("You gained {} HP!".format(hp))
            self.hp=self.hp+hp
            return(True)
        else:
            write("HP is already full")
            return(False)
    def Add_mp(self,mp):
        if self.mp<self.maxMp:
            if (self.mp+mp)>self.maxMp:
                mp=self.maxMp-self.mp
            write("You gained {} MP!".format(mp))
            self.mp=self.mp+mp
            return(True)
        else:
            write("MP is already full")
            return(False)
    def Set_cool_down(self,coolTime):
        self.coolDown=coolTime
    def Increase_maxHp(self,increase):
        self.maxHp+=increase
    def Decrease_maxHp(self,decrease):
        self.maxHp-=decrease
    def Increase_maxMp(self,increase):
        self.maxMp+=increase
    def Decrease_maxMp(self,decrease):
        self.maxMp-=decrease
    def Change_gear(self,what):
        if isinstance(what,armour.armour):
            self.armour=what
        if isinstance(what, weapons.weapon):
            self.weapon=what
# player1=Player(120,500)#omega arts
#allPlayers=[player1]