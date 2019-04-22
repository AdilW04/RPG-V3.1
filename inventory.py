#0=consum,
#1=weapons,
#2=mats
from constants import *
from write_text import write
from time import sleep
from unrecognised import Invalid
color=BOLD+ORANGE+NONEB
names=[
    [["Owl Potion","Nightingale Potion","Phoenix Potion"],["Owl Decoction", "Nightingale Decoction","Phoenix Decoction"]],
    [["{}Dull Dagger{}".format(color,NORMAL),"{}Ancient Bow{}".format(color,NORMAL),"{}Rusty Sword{}".format(color,NORMAL),"{}Mossy Warhammer{}".format(color,NORMAL)],["{}Creased Shirt{}".format(color,NORMAL),"{}Emmanuel Uniform{}".format(color,NORMAL),"{}Lucky Jumper{}".format(color,NORMAL),"{}Biker Jacket{}".format(color,NORMAL)]],
    []
]
#toxicities=[[30,45,55],[30,45,55]]
values=[
    [[60,120,180],[60,120,180]],
    [[450,565,608,680],[25,40,245,240]],
    []
    ]
rejuvination=[[80,160,300],[40,120,250]]

class item:
    def __init__(self,c,t,i):#class,type,index for 3d arrays
        self.name=names[c][t][i]
        self.value=values[c][t][i]
        self.sellVal=round(self.value/2.5)



class materials(item):
    def __init__(self,i):
        super().__init__(i)
    



class consumables(item):
    def __init__(self,t,i):
        super().__init__(CONSUMABLES,t,i)
        self.coolDown=4
        self.type=t
        self.index=i
        self.rejuvination=rejuvination[t][i]
    def Increase_CD_time(self,amount):
        self.coolDown=self.coolDown+amount
    def Decrease_CD_time(self,amount):
        self.coolDown=self.coolDown-amount
    def Consume(self,player):
        player.Set_cool_down(self.coolDown)
    def Use(self,player):
        if player.inventory.amountOwned[CONSUMABLES][self.type][self.index]>0 and player.coolDown<=0:
            success=self.Rejuvinate(player)
            if success:
                player.inventory.Lose(CONSUMABLES,self.type,self.index,1)
                self.Consume(player)
                player.loop=False
                return(False,False)
            else:
                return(True,True)
        else:
            write("You don't have any {}s".format (self.name)if player.inventory.amountOwned[CONSUMABLES][self.type][self.index]<=0 else "You cannot stomach another one of these yet...")
            return(True,True)
            
    

class decoctions(consumables):
    def __init__(self,i):
        super().__init__(DECOCTIONS,i)
    def Rejuvinate(self,player):
        write("{} uses {} to restore MP!".format(player.name,self.name))
        success=player.Add_mp(self.rejuvination)
        return(success)

class potions(consumables):
    def __init__(self,i):
        super().__init__(POTIONS,i)
    def Rejuvinate(self,player):
        write("{} uses {} to heal HP!".format(player.name,self.name))
        success=player.Add_hp(self.rejuvination)
        return(success)
class equipables(item):
    def __init__(self,t,i):
        super().__init__(EQUIPPABLES,t,i)
    def Equip(self,player):
        player.Change_gear(self)





owlPot=potions(OWL_POT)
nightPot=potions(NIGHT_POT)
pheoPot=potions(PHEO_POT)
owlDec=decoctions(OWL_DEC)
nightDec=decoctions(NIGHT_DEC)
pheoDec=decoctions(PHEO_DEC)
class inventory:
    def __init__(self):
        self.amountOwned=[
            [[0,0,0],[0,0,0]],
            [[0,0,0,0],[0,0,0,0]],
            [[]]
        ]
        self.items = [
            [[], []],
            [[],[]],
            []
        ]
    def Show(self,type):
        for item in self.items[type]:
            t=self.items[type].index(item)
            for index in item:
                i=self.items[type][t].index(index)
                print(">  ",index.name,"x"+str(self.amountOwned[type][t][i]))
                sleep(0.02)
    def Access_in_battle(self,player):
        print(self.items)
        choice_use={"BACK":self.Back}
        self.Show(CONSUMABLES)
        print(">  BACK")
        loop=True
        while loop:
            action=input("What item would you like to use? ")
            action=action.upper()
            for item in self.items[CONSUMABLES]:
                for i in item:
                    choice_use.update({i.name.upper():self.items[CONSUMABLES][i.type][i.index].Use})
                    #nts existance of an object is different when stored in different data structures eg:
                    #a=obj       list=[a,b,c]
                    #b=obj       a=!list[0]
                    #c=obj       they exist as two separate objects
            loop,x=choice_use.get(action,Invalid)(player)#x catches stray boolean
    def Back(self,*args):
        return(False,True)
    def Gain_item(self,clas,type,itemNo,itemObj):
        self.items[clas][type].append(itemObj)
        self.Add(clas,type,itemNo,1)
    def Gain_equipable(self,type,itemObj):
        self.items[EQUIPPABLES][type].append(itemObj)
    def Add(self,clas,type,index,amount):
        self.amountOwned[clas][type][index]+=amount
    def Lose(self,clas,type,index,amount):
        self.amountOwned[clas][type][index]-=amount


items=inventory()
    



          