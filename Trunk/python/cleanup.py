
import os

def removeFolder(dir,recursion):
  if(not os.path.exists(dir)):
    return
  if(not os.path.isdir(dir)):
    return
  subs = os.listdir(dir)
  for sub in subs:
    print (sub)
    if(os.path.isdir(sub)):
      removeFolder(os.path.join(dir,sub),recursion)
    else:
       print ("remove: %s" %os.path.join(dir,sub))
       os.remove(sub)




if __name__=="main":
  removeFolder("J:\\Test",1)
