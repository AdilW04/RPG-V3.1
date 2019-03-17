import login
from constants import *
from write_text import write
from time import sleep
import players
from random import randint, choice
color=BOLD+RED+NONEB
name=["{}Raging Roach{}".format(color,NORMAL),"{}Crumblin Cannon{}".format(color,NORMAL),"{}Serious Sasquatch{}".format(color,NORMAL),"{}Angry Albatross{}".format(color,NORMAL),"{}Ogled{}".format(color,NORMAL),"{}Basalisk{}".format(color,NORMAL)]
hp=[75,10,100,150,100,100]#[75,10,100,150,999,100]
atk=[10,100,14,20,0,36]
miss=[10,35,12,16,10,25]
crit=[11,12,13,8,10,5]
money=[500,600,800,1200,1250,1500]
abbs=["{}RR".format(color),"{}CC".format(color),"{}SS".format(color),"{}AA".format(color),"{}OGLD".format(color),"{}BSLK".format(color)]#abreviations
enemyTechs=[]#variable for techs enemies can use, will change through the game when new techs get unlocked

class enemy:
    def __init__(self,i,player,techs):
        self.name=name[i]
        self.atk=atk[i]#changable when hero defends
        self.ATK=atk[i]#this one is a constant it dosnt change once established
        self.miss=miss[i]
        self.crit=crit[i]
        self.hp=hp[i]
        self.opponent=None
        self.activeEffects=[]
        self.availableTechs=techs#available tech objects including enemies own attack
#       self.damageDealt=opponentsWeapon.get_Atk()
        self.availableTechs.append(self)
        self.isEnhanced=False
        self.abb=abbs[i]
        self.color="\033[0;37;31m"
        self.isFrozen=False
        self.isDizzy=False
        self.money=money[i]
        self.opponent=player
    def Flip(self,**kwargs):#function that allows me to change player variables based on paramaters
        if list(kwargs.keys())[0]=="isEnhanced":
            self.isEnhanced=kwargs.get("isEnhanced")#gets "isDefending" from dicitionsry key and value entered into the brackets when called 
        if list(kwargs.keys())[0]=="isFrozen":
            self.isFrozen=kwargs.get("isFrozen")
        if list(kwargs.keys())[0]=="isDizzy":
            self.isDizzy=kwargs.get("isDizzy")
        
#    def Reset(self):#enemy always end turn
#        self.atk=self.ATK#resets atk, may as well put it here
    
    def Enemy_turn(self):
      self.atk=self.ATK
      write("Its {}'s turn now".format(self.name))
      #adds object to list if not in it so no duplicates every enemy turn  

      #   for tech in self.availableTechs:
      #   tech.Use_tech(self)  
      for activeEffect in self.activeEffects:
          activeEffect.effectDamage(self)  

      #self.opponent=opponent
      if self.isFrozen==False and self.isDizzy==False:
          tech=choice(self.availableTechs)
          tech.Use_tech(self,self.opponent)
    
    
    def Use_tech(self,*args):#accepts an amount of paramaters  
      self.atk=randint(round(self.atk-(self.atk*0.1)),round(self.atk+(self.atk*0.1)))
      missRNG=randint(1,100)
      critRNG=randint(1,100)
      global isCrit
      heroName = login.Get_heroName()
      write(self.name+" is attacking "+heroName)
      sleep(SLP)
      if missRNG<=self.miss:
          write(self.name+" missed!")
          return()
      if critRNG<=self.crit:
          write(self.name+" got a critical!")
        #   write("It did a damage of ",self.atk*2,"!")
          self.Do_dmg(self.atk*2,True)
          return()
      else:
          self.Do_dmg(self.atk)
          return()
 
    # def Get_atk(self):
    #     global isCrit
    #     if isCrit==True:#if get crit
    #         isCrit=False
    #         return(self.atk*2)
    #     else:
    #         return(self.atk)
    def Do_dmg(self,damage,*args):
        if self.isEnhanced==True:
            damage=damage*3
        #might add more stuff that effects damage
        self.opponent.Lose_hp(damage,True)if True in args else self.opponent.Lose_hp(damage,False)
            
    def Lose_hp(self,damageDealt):
        write("it did {} damage!".format(damageDealt))
        #damageDealt=self.opponent.weapon.Get_atk()
        #reset weapon stats to default when rng or armour every turn
        #self.opponent.weapon.atk=self.opponent.weapon.ATK
        self.hp=self.hp-damageDealt
    def Get_enemyName(self):
        return(self.name)

# test=enemy(RAGING_ROACH)
# testB=enemy(SERIOUS_SASQUATCH)



