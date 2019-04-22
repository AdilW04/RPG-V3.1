from write_text import write
from constants import *
loop=None
def Invalid(*args):
    global loop
    write("{} ARE YOU BLIND OR SOMETHING?!".format(BOLD+RED+NONEB))
    write("{} TYPE SLOWER NEXT TIME SO YOU DON'T MISSPELL, CAPICHE?".format(BOLD + RED + NONEB))
    loop=True
    return(True,False)