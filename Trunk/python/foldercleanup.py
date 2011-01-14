
import os
import os.path
import datetime
  
def getOption():
  from optparse import OptionParser
  
  des   = "clean up the folder with some options"
  prog  = "foldercleanup"
  ver   = "%prog 0.0.1"
  usage = "%prog [options] foldername"
  
  p = OptionParser(description=des, prog=prog, version=ver, usage=usage,add_help_option=True)
  p.add_option('-d','--days',action='store',type='string',dest='days',help="keep the subfolders which are created in recent %days% days")
  p.add_option('-k','--keepfile',action='store',type='string',dest='keepfile',help="keep the subfolders which are recorded in text file %keepfile% ")
  options, arguments = p.parse_args()
  
  if len(arguments) != 1:
    print("error: must input one directory as only one parameter ")
    return
  
  return options.days, options.keepfile, arguments[0]  

 
def preCheckDir(dir):
  if(not os.path.exists(dir)):
    print("error: the directory your input is not existed")
    return
  if(not os.path.isdir(dir)):
    print ("error: the parameter your input is not a directory")
    return
    
  return os.path.abspath(dir)
  
def isKeepByDay(dir, day):
  indays = False
  if( day is not None) :
    t = os.path.getctime(dir)
    today = datetime.date.today()
    createdate = datetime.date.fromtimestamp(t)
    indate = today - datetime.timedelta(days = int(day))
    print (createdate)
    if(createdate >= indate):
      indays = True
  print (indays)
  return indays
  
def isKeepByKeepfile(dir, keepfile):
  needkeep = False
  print (dir)
  if (keepfile is not None):
    try :
      kf = open(keepfile,"r")
      for f in kf.readlines():
        print (f)
        if (dir.upper().endswith("\\" + f.strip().upper())):
          needkeep = True
      kf.close()
    except:
      print ("error: keep file cannot be opened")
  print(needkeep)
  return needkeep
    
def removeSubFolders(dir, day, keepfile):
  subdirs = os.listdir(dir)
  for subdir in subdirs:
    subdir = os.path.join(dir,subdir)
    if ( not os.path.isdir(subdir)):
      continue
    print("----------------------")
    if( (not isKeepByDay(subdir, day))and (not isKeepByKeepfile(subdir, keepfile))):
      print("remove subfolder: " + subdir)
      import shutil
      shutil.rmtree(subdir,True)
    
def FolderCleanUp():
  (day, keepfile, dir) = getOption()
  dir = preCheckDir(dir)
  if dir is None:
    return
  removeSubFolders(dir,day,keepfile)
  
def KeepLastNumZips(num)
    def extractTime(f):
        return os.path.getctime(f)

    zipfiles = [os.path.join(zipdir, f)
                for f in os.listdir(zipdir)
                if os.path.splitext(f)[1] == ".zip"]
    if len(zipfiles) > num:
        zipfiles.sort(key=extractTime, reverse=True)
        for i in range(num, len(zipfiles)):
            os.remove(zipfiles[i])

if __name__=='__main__':
  FolderCleanUp()
