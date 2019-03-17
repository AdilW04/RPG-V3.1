from write_text import write
from constants import *
loop=None
def Invalid(*args):
    global loop
    write("{}Invalid".format(BOLD+RED+NONEB))
    loop=True
    return(True,False)