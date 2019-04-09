from write_text import write
from constants import *
import login
from random import randint
from unrecognised import Invalid
from time import sleep
import enemies
import players

names=["Enhance","Infernix","Hurrix","Chillix","Voltix"]
elements=[None,"FIRE","WIND","ICE","LIGHTNING"]
effectNames=["ENHANCED","BURN","DIZZINESS","FREEZE","STUN"]
atk=[0,20,40,60,60]
mp=[30,40,55,50,75]
effectChances=[0,45,23,20,50]
effectCounters=[[2,3],[2,3],[1,2],[2,3],[2,4]]
techTypes=["statBuff","offensive","statDebuff","statDebuff","statDebuff"]
properties=["Enhancing","Fire Breathing","Hurricane Conjuring","Ice Manipulating","Lightning Producing"]#for enemy

class magic:
  def __init__ (self,i,player):#pass in self to omega arts and to this
    self.atk=atk[i]
    self.ATK=atk[i]
    self.elements=elements[i]
    self.name=names[i]
    self.mp=mp[i]
    self.player=player
    self.effectName=effectNames[i]
    self.effectCounter=0#sets the variable for effect counter to avoid a petential name or attribute error
    # self.effectChance=randint(1,100)
    self.effectChances=effectChances[i]
    self.effectCountRange=effectCounters[i]
    self.techType=techTypes[i]
    self.monsterProperty=properties[i]
  

  def Use_tech(self,user,target): 
      global loop
      if isinstance(user,players.Player) and user.mp<self.mp-user.armour.mp:
          write("{}{} does not have enough MP to use {}".format(BOLD+RED+NONEB,user.name,self.name))
          return(True,True) 
      write("{} uses {} on {}".format(user.name,self.name,target.name) if self.techType!="statBuff" else "{} uses {}".format(user.name,self.name))
      if self.techType!="statBuff":
          self.atk=self.ATK
          self.atk=randint(self.atk-round(self.atk*0.15),self.atk+round(self.atk*0.15))
          effectRNG=randint(1,100)
          if isinstance(user,enemies.enemy):
              user.Do_dmg(self.atk,False)#not a regular attack its magic instead
          else:
              user.Do_dmg(self.atk)
      
      #                            prevents you from getting burned,poisoned etc twice
      if self.techType=="statBuff" or effectRNG<=self.effectChances and self not in target.activeEffects:
          if self.techType=="statBuff" and self in user.activeEffects:
              write("{}'s duration has extended!".format(self.name))
              self.effectCounter=self.effectCountRange[1]
          else:
            write("{} inflicted {} on {}! ".format(user.name,self.effectName,target.name)if self.techType!="statBuff" else "{} is now {}".format(user.name,self.effectName))
            self.effectCounter=randint(self.effectCountRange[0],self.effectCountRange[1])
            
            target.activeEffects.append(self) if self.techType!="statBuff" else user.activeEffects.append(self)
      if isinstance(user,players.Player):
           user.Lose_mp(self.mp)#might change if i want enemy t have mp
      return(False,False)
  
  def effectDamage(self,user):
      def Enhance_effect():
          user.Flip(isEnhanced=True)
          return(0)
      def Hurrix_effect():
          user.Flip(isDizzy=True)
          RNG=randint(1,100)
          money=randint(1,150)
          if RNG<=25 and money<=user.money:
              write("{} throws {} YIELD towards {} out of confusion".format(user.name,money,user.opponent.name))
              user.Lose_money(money)
              user.opponent.Add_money(money)
              return(0)
          else:
              #write("{} is dizzy, {} cannot move!".format(user.name,user.name))
              return(0)
      def Chillix_effect():
          if isinstance(user,enemies.enemy):
              write("{} is frozen, {} can't move!".format(user.name,user.name))
          user.Flip(isFrozen=True)
          return(0) 
      def Infernix_effect():
          damage=randint(7,13)
          write("{} is on fire! (litteraly!)".format(user.name))
          return(damage)

      
      if self.effectCounter==0:
          write("{}'s {} effect has worn off".format(user.name,self.effectName))
          user.activeEffects.remove(self)
          if self.name=="Enhance": 
              user.Flip(isEnhanced=False)
          if self.name=="Chillix":
              user.Flip(isFrozen=False)
          if self.name=="Hurrix":
              user.Flip(isDizzy=False)
          return()
      
      
      effectResponses={
          "Enhance":Enhance_effect,
          "Infernix":Infernix_effect,
          "Chillix":Chillix_effect,
          "Hurrix":Hurrix_effect
      }
      damage=effectResponses.get(self.name)()

      if self.techType=="offensive":
        if isinstance(user,players.Player):
            user.Lose_hp(damage,False,"effectDmg")#because not regular atk
        else:
            user.Lose_hp(damage)#enemy loses hp

        #   try:
        #       user.Lose_hp(damage,False,"effectDmg")#because not regular atk
        #   except TypeError:
        #       user.Lose_hp(damage)
      self.effectCounter=self.effectCounter-1
class omegaArts:
    def __init__(self,player):
        global enhance
        global infernix
        global chillix
        global hurrix
        enhance=magic(ENHANCE,player)
        infernix=magic(INFERNIX,player)
        chillix=magic(CHILLIX,player)
        hurrix=magic(HURRIX,player)
        self.techs={
            enhance:False,
            infernix:False,
            chillix:False,
            hurrix:False
        }
        self.player=player
    
    def Back(*args):
        return(False,True)
    
    def Omega_arts(self,*arg):
        global loop
        for tech in self.techs:
            if self.techs.get(tech)==True:
                sleep(0.1)
                if self.player.mp>=(tech.mp-self.player.armour.mp):
                    print("> {} -{}MP".format(tech.name,tech.mp-self.player.armour.mp))
                else:
                    print("{}> {} -{}MP{}".format(NONE+GREY+NONEB,tech.name,tech.mp-self.player.armour.mp,NORMAL))
                sleep(0.1)
        print("> BACK")
        sleep(0.1)
        loop=True
        while loop==True:

            write("  Which technique would you like to use")
            chosen=input("  ")
            chosen=chosen.upper()
            results={
            "ENHANCE":list(self.techs.keys())[0].Use_tech if self.techs.get(list(self.techs.keys())[0]) else Invalid,
            "INFERNIX":list(self.techs.keys())[1].Use_tech if self.techs.get(list(self.techs.keys())[1]) else Invalid,
            "CHILLIX":list(self.techs.keys())[2].Use_tech if self.techs.get(list(self.techs.keys())[2]) else Invalid,
            "HURRIX":list(self.techs.keys())[3].Use_tech if self.techs.get(list(self.techs.keys())[3]) else Invalid,
            "BACK":self.Back
            }
            loop,self.player.loop=results.get(chosen,Invalid)(self.player,self.player.opponent)
    
    
