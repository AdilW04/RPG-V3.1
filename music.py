import pygame
from time import sleep
pygame.init()
def music(play,*args):
    try:
        pygame.display.set_mode((1,1))
    except pygame.error:
        return()
    if play==True:
        song=pygame.mixer.music.load(args[0])
        pygame.mixer.music.play(args[1])
    if play==False:
        pygame.mixer.music.stop()
