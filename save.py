from constants import *
import pickle
from write_text import write
import loading
import main

def Save(player):
    f=open(player.name+RPG,"wb")
    pickle.dump(player,f)
    loading.Loading_animation(7,"Saving complete! See you later {}!".format(player.name),"SAVING please wait")
def Load():
    f=open(login.Get_heroName+RPG,"wb")
    player=pickle.load(f)
    loading.Loading_animation(randint(2,12),"Hello {}!".format(player.name))
    return(player)
#deprecated