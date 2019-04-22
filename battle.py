import music
from constants import *
import win_lose
import threading
        # loop=True
        # player.activeEffects.clear()
        # player.isFrozen=False
        # player.isEnhanced=False
        # while loop==True:
        #     player.Action()
        #     loop=win_lose.Win_lose(player)
        #     if loop==False:
        #         break
        #     player.opponent.Enemy_turn()
        #     loop=win_lose.Win_lose(player)
def Battle(player,opponent):
    music.Music(PLAY,player.stage.battleTheme,-1)
    player.activeEffects.clear()
    player.isFrozen=False
    player.isEnhanced=False
    while True:
        if win_lose.Win_lose(player)==False:
            break
        else:
            print()
            player.Action()
            player.Sub_turn()
        if win_lose.Win_lose(player)==False:
            break
        else:
            print()
            opponent.Enemy_turn()

