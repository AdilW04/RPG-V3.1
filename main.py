import players
import login
from enemies import *
from weapons import *
import loading
from random import randint
from music import music
from constants import *
import pickle
from write_text import write
#logimusic(PLAY,"taizai.wav",-1)

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


player1.stage.start(player1)

#loading.Loading_animation(5,"Good bye {}LOSER!                                             ".format(BOLD+RED+NONEB),"EXITING GAME, Any unsaved progress will be {}LOST ".format(UNDERLINE+RED+NONEB))
#pass