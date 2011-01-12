
import os

class def MyEnv:
  envFile = "c:\\myenv.txt"
  envs = {}
  
  def SetEnvFile(self, filename) : 
    envFile = filename
    
  def Save(self) :
    outf = open(envFile, "w")
    if not outf:
      print ("env file cannot be opened for write!")
    for k, v in this.ens.items() :
      outf.write(k + "=" + v)
    outf.close()
    
  def Load(self) :
    inf = open(envFile, "r")
    if not inf:
      print ("env file cannot be opened for open!")
    for line in inf.readlines() :
      k, v = line.split("=")
      envs[k] = v
    inf.close()
    
  def AddEnv(self, k, v) :
    envs[k] = v
    
  def RemoveEnv(self, k) :
    del envs.remove[k]
    
  def PrintAll() :
    for k, v in envs.item():
      print k + "=" + v
   
if __name__ == "__main__" :
  myEnv = MyEnv()
  myEnv.SetEnvFile("c:\\myenv.txt")
  myEnv.PrintAll()
  