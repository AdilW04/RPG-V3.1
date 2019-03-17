from write_text import *
from constants import *
from random import randint
import login
import enemies
import players
color=BOLD+ORANGE+NONEB
name=["{}Dull Dagger{}".format(color,NORMAL),"{}Ancient Bow{}".format(color,NORMAL),"{}Rusty Sword{}".format(color,NORMAL),"{}Mossy Warhammer{}".format(color,NORMAL)]
atk=[9,13,15,16]
miss=[10,16,7,14]
crit=[12,15,16,20]
chainCount=[5,6,7,8]
index=[0,1,2,3,4,5,6,7,8,9,10]
values=[450,565,608,680]

class weapon:
    def __init__(self,i,player):
        self.name=name[i]
        self.atk=atk[i]
        self.ATK=atk[i]
        self.miss=miss[i]
        self.crit=crit[i]
        self.chainCount=0#crit chain
        self.i=index[i]
        self.value=values[i]
        self.sellVal=round(values[i]/1.4)

        self.player=player
    def Attack_enemy(self,*arg):
        global isCrit
        self.player.loop=False
        self.atk=randint(round(self.atk-(self.atk*0.1)),round(self.atk+(self.atk*0.1)))
        heroName=login.Get_heroName()
        write(heroName + " uses " + self.name + " to attack " + self.player.opponent.name)
        isCrit = False
        missRNG=randint(1,100)
        critRNG=randint(1,100)
        sleep(SLP)
        if missRNG<=self.miss:
            write("You missed!")
            self.chainCount==0
            self.crit=crit[self.i]
            return()
        if critRNG<=self.crit:             
            if self.chainCount==0:

                self.chainCount=chainCount[self.i]
            if self.chainCount>0:
                self.chainCount=self.chainCount-1
                self.crit=self.crit+19
            write("You got a critical!")
            isCrit=True
            self.player.Do_dmg(self.atk*2)
            
            return()
        else:
            self.chainCount==0
            self.crit=crit[self.i]
            isCrit=False
            self.player.Do_dmg(self.atk)
            return()
        
    def Get_atk(self):
        global isCrit
        if isCrit==True:#if get crit
            isCrit=False
            return(self.atk*2)
        else:
            return(self.atk)
#dullDagger=weapon(DULL_DAGGER,self.opponent)
#not recognising opponent variable

