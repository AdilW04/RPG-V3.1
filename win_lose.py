from write_text import write
import random
from constants import *
from music import Music
def Win_lose(player):
    if player.hp<=0:
        player.hp=0
        Game_over(player)
    elif player.opponent.hp<=0:
        player.opponent.hp=0
        Win(player)
        Music(PLAY,"victory_a.mp3",-1)
        return(False)
    else:
        return(True)
def Game_over(player):
    write("OH NO!!")
    write("HOW AWFUL!!!")
    write("You have died!")#to be expanded upon (load last save data)
    quit()

        
    
def Win(player):
    write("{}You win!".format (DIM+WHITE+ORANGEB))
    #player.stage.distance=player.stage.distance-random.randint(5,20)#temp
    player.activeEffects.clear()
