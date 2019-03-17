import sys
from time import sleep
from constants import *
def Loading_animation(iterations,msg,msg2):
    if REPL==True:
        for i in range(iterations):
            sys.stdout.write("\r{}|{} {}.  {}|{}".format(BOLD+BLUE+NONEB,NORMAL,msg2,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
            sys.stdout.write("\r{}\{} {}.. {}\\{}".format(BOLD+BLUE+NONEB,NORMAL,msg2,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
            sys.stdout.write("\r{}-{} {}.. {}-{}".format(BOLD+BLUE+NONEB,NORMAL,msg2,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
            sys.stdout.write("\r{}/{} {}.  {}/{}".format(BOLD+BLUE+NONEB,NORMAL,msg2,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
        msg=str(msg)
        for char in"\r> "+msg+"       \n":
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.03)
    else:
        pass
def Loading_animation2():
    done=False
    if REPL==True:
        while done==False:
            sys.stdout.write("\r{}|{} Loading please wait.  {}|{}".format(BOLD+BLUE+NONEB,NORMAL,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
            sys.stdout.write("\r{}\{} Loading please wait.. {}\\{}".format(BOLD+BLUE+NONEB,NORMAL,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
            sys.stdout.write("\r{}-{} Loading please wait.. {}-{}".format(BOLD+BLUE+NONEB,NORMAL,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
            sys.stdout.write("\r{}/{} Loading please wait.  {}/{}".format(BOLD+BLUE+NONEB,NORMAL,BOLD+BLUE+NONEB,NORMAL))
            sleep(0.1)
        for char in"\r> DONE!                  \n":
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.03)
