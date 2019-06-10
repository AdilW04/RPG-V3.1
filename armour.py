from constants import *
import inventory
names=["Creased Shirt","Emmanuel Uniform","Lucky Jumper","Biker Jacket"]
reductions=[0,2,0,4]
miss=[0,1,8,3]
crit=[0,2,45,5]
mp=[0,5,10,8]
values=[25,40,245,240]
class armour(inventory.equipables):
    def __init__(self,i):
        super().__init__(ARMOUR,i)
        self.reduction=reductions[i]
        self.miss=miss[i]
        self.crit=crit[i]
        self.mp=mp[i]



    
        