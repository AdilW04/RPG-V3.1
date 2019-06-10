import pygame
import threading
import loading
DULL_DAGGER=0
ANCIENT_BOW=1
RUSTY_SWORD=2
MOSSY_WARHAMMER=3

RAGING_ROACH=0
CRUMBLIN_CANNON=1
SERIOUS_SASQUATCH=2
ANGRY_ALBATROSS=3
OGLED=4
BASALISK=5

CREASED_SHIRT=0
EMMANUEL_UNIFORM=1
LUCKY_JUMPER=2
BIKER_JACKET=3

SLP=0

ENHANCE=0
INFERNIX=1
HURRIX=2
CHILLIX=3
BOLTIX=4

NONE=0
FIRE=1
WIND=2
LIGHTNING=3

PERILOUS_PLAINS=0
DUSTY_DUNES=1
MYTHRIL=2
RUSTIC_RUINS=3

OWL_POT=0
NIGHT_POT=1
PHEO_POT=2
OWL_DEC=0
NIGHT_DEC=1
PHEO_DEC=2

LOCATION=""#//home//runner//save_files//"#folder containing savefiles
RPG=" RPG V3_1.txt"

PLAY=True
STOP=False
done=False

try:
    pygame.init()
    pygame.display.set_mode((1,1))
    pygame.quit()
    REPL=False
except pygame.error:
    REPL=True
if REPL:
    NONE="\033[0"
    BOLD="\033[1"
    DIM="\033[2"
    ITALICS="\033[3"
    UNDERLINE="\033[4"

    BLACK=";30"
    RED=";31"
    GREEN=";32"
    ORANGE=";33"
    BLUE=";34"
    PURPLE=";35"
    CYAN=";36"
    GREY=";37"
    WHITE=";38"


    BLACKB=";40m"
    PINKB=";41m"
    GREENB=";42m"
    ORANGEB=";43m"
    BLUEB=";44m"
    PURPLEB=";45m"
    CYANB=";46m"
    GREYB=";47m"
    NONEB=";48m"

    NORMAL="\033[0;38;48m"
else:
    NONE=""
    BOLD=""
    DIM=""
    ITALICS=""
    UNDERLINE=""

    BLACK=""
    RED=""
    GREEN=""
    ORANGE=""
    BLUE=""
    PURPLE=""
    CYAN=""
    GREY=""
    WHITE=""


    BLACKB=""
    PINKB=""
    GREENB=""
    ORANGEB=""
    BLUEB=""
    PURPLEB=""
    CYANB=""
    GREYB=""
    NONEB=""

    NORMAL=""

CONSUMABLES=0
MATERIALS=2
EQUIPPABLES=1

POTIONS=0
DECOCTIONS=1

WEAPONS=0
ARMOUR=1



    

