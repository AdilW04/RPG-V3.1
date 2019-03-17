import pygame
from time import sleep
pygame.init()
def Music(play,*args):
    try:
        pygame.display.set_mode((1,1))
    except pygame.error:
        return()
    if play==True:
        # pygame.mixer.music.stop()
        song=pygame.mixer.music.load(args[0])
        pygame.mixer.music.play(args[1])
    if play==False:
        pygame.mixer.music.stop()
# def Sound(sound):
#     try:
#         pygame.display.set_mode((1,1))
#     except pygame.error:
#         return()
#     sound=pygame.mixer.Sound(sound)
#     sound.play()
