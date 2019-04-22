import login
import enemies
import weapons
import loading
import armour
from random import randint
from music import Music
from constants import *
import pickle
from write_text import write
import players
import inventory
#Music(PLAY,"perilous_plains.mp3",-1)
#looping: method that recieves player objact as parameter is responsible for changing objacts loop attribute
reg=login.main()

if reg:
    player1=players.Player(120,500)
    #player1.Create_main_objs()
    player1.Unlock_OA()
else:
    name=login.Get_heroName()
    try:
        f=open(name+RPG,"rb")
        player1=pickle.load(f)
        #player1.Create_main_objs()
        player1.Unlock_OA()
    except EOFError as errorName:
        write("....")
        write("It seems something is wrong with your file")
        write("[",errorName,"]")
        loading.Loading_animation(randint(2,12),"Complete!                                 ".format(login.user),"CREATING NEW FILE Please wait")
        player1=players.Player(120,500)
        #player1.Create_main_objs()
        player1.Unlock_OA()
    except FileNotFoundError as errorName:
        write("....")
        write("It seems something is wrong with your file")
        write ("[",errorName,"]")
        loading.Loading_animation(randint(2,12),"Complete!                                 ".format(login.user),"CREATING NEW FILE Please wait")
        login.Register(login.Get_heroName())
        player1=players.Player(120,500)
        #player1.Create_main_objs()
        player1.Unlock_OA()
# playersList[
#     player1
# ]
player1.inventory.Gain_item(CONSUMABLES,POTIONS,OWL_POT,inventory.owlPot)
weapon=weapons.weapon(DULL_DAGGER)
player1.inventory.Gain_equipable(WEAPONS,weapon)
player1.Change_gear(player1.inventory.items[EQUIPPABLES][WEAPONS][DULL_DAGGER])
armour=armour.armour(CREASED_SHIRT)
player1.inventory.Gain_equipable(ARMOUR,armour)
player1.Change_gear(player1.inventory.items[EQUIPPABLES][ARMOUR][CREASED_SHIRT])
player1.Change_stage(0)

player1.stage.start(player1)

#loading.Loading_animation(5,"Good bye {}LOSER!                                             ".format(BOLD+RED+NONEB),"EXITING GAME, Any unsaved progress will be {}LOST ".format(UNDERLINE+RED+NONEB))
#pass
