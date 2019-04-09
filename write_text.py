import sys
from time import sleep
from constants import *
try:
    pygame.init()
    pygame.display.set_mode((1,1))
    pygame.quit()
    REPL=False
except pygame.error:
    REPL=True

def write(*arg):
    output = ""
    for argument in arg:
      argument=str(argument)
      output=output+argument
    if REPL==True:
        output=output+"\033[0;37;39m"
    output=output+"\n"
    
    for char in output:
          sys.stdout.write(char)
          sys.stdout.flush()
          sleep(0.04)
