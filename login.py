from write_text import write
from constants import *
from time import sleep
import tutorial
import sys
from constants import *
from unrecognised import Invalid
import players
from write_text import write

def main():
  global loop
  loop=True
  while loop==True:
    write("\nDo you want to {}register{} or {}login{}?".format(BOLD+GREEN+NONEB, NORMAL,BOLD+GREEN+NONEB, NORMAL))
    ans=input()
    ans=ans.upper()
    res={
      "REGISTER":Register,
      "LOGIN":Login
      }
    reg=res.get(ans,Invalid)()
  return(reg)

def Register(*args):
  global pWord  
  args=list(args)
  global user  
  global loop
  while True:
      if args==[]:
        while True:      
            write("Please enter a {}username".format(UNDERLINE+CYAN+NONEB))
            user=input("> ")
            players=open("users.txt","r")
            registered=players.readlines()
            players.close()
            if user+"\n" in registered:
              write("That name is already taken")
            else:
              write("please enter your {}password".format(UNDERLINE+CYAN+NONEB))
              pWord=input("> ")
              break
        players=open("users.txt","a")
        players.write(user+"\n")
        players.close()
        passes=open("passwords.txt","a")
        passes.write(pWord+"\n")
        passes.close()
      else:
        user=args[0]
        user

      playerSave=open(LOCATION+user+RPG,"a")
      playerSave.close()
      write("{}SUCCESS!".format(BOLD+GREEN+NONEB))
      write("welcome to RPG V3.1 {}!".format(user))
      loop=False  
      return(True)
      break

def Login():
  global loop
  global user
  while True:
    write("please enter your {}username".format(UNDERLINE+CYAN+NONEB))
    user=input("> ")
    write("please enter your {}password".format(UNDERLINE+CYAN+NONEB))
    pWord=input("> ")
    players=open("users.txt","r")
    registeredUsers=players.readlines()
    players.close()
    passwords=open("passwords.txt","r")
    registeredPass=passwords.readlines()
    passwords.close()
    #registeredUsers[-1]=registeredUsers[-1]+"\n"
    #registeredPass[-1]=registeredPass[-1]+"\n"
    match=False
    for passW,userName in zip(registeredPass,registeredUsers):
      if passW==pWord+"\n" and userName==user+"\n":
        write("{}SUCCESS!".format(BOLD+GREEN+NONEB))
        #(temp)#load dumped obj and set that obj as player1
        match=True
        #break
    if match==True:
      loop=False  
      return(False)
    else:
      write("Your username or password is incorrect")
      loop=True
      return()
      
def Get_heroName():
    global user
    return(user)