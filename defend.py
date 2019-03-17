from write_text import write
import login
class defendClass:
  def __init__(self,player):#takes in player object
    self.player=player#player in question
    self.isGuarding=False#ready to attack
  def Guard(self,*arg):#means that it can take in anything no matter what, perfect for switchcases
    name=login.Get_heroName()
    self.isGuarding=True
    write("{}'s guard is up".format(name))
    self.player.loop=False
  
  def Restore(self):
    name=login.Get_heroName()
    write("{}'s guard is no longer up".format(name))
    self.isGuarding=False
    

  
