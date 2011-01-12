
import os

class MyEnv:

  def __init__(self):
    self.envFile = "c:\\myenv.txt"
    self.envs = {}
  
  def SetEnvFile(self, filename) : 
    self.envFile = filename
        
  def Save(self) :
    outf = open(self.envFile, "w")
    if not outf:
      print ("env file cannot be opened for write!")
    for k, v in self.envs.items() :
      outf.write(k + "=" + v + "\n")
    outf.close()
    
  def Load(self) :
    inf = open(self.envFile, "r")
    if not inf:
      print ("env file cannot be opened for open!")
    for line in inf.readlines() :
      k, v = line.split("=")
      self.envs[k] = v
    inf.close()
    
  def ClearAll(self) :
    self.envs.clear()
    
  def AddEnv(self, k, v) :
    self.envs[k] = v
    
  def RemoveEnv(self, k) :
    del self.envs[k]
    
  def PrintAll(self) :
    for k, v in self.envs.items():
      print ( k + "=" + v )
   
if __name__ == "__main__" :
  myEnv = MyEnv()
  myEnv.SetEnvFile("c:\\myenv.txt")
  myEnv.Load()
  myEnv.AddEnv("MYDIR", "c:\\mydir")
  myEnv.AddEnv("MYDIR2", "c:\\mydir2")
  myEnv.AddEnv("MYDIR3", "c:\\mydir3")
  myEnv.Save()
  myEnv.PrintAll()
  