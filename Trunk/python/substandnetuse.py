
import os
import subprocess
  
def RunCommand(cmd):
  return subprocess.call(cmd)
  
def RunCommandWithOutput(cmd):
  p=subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (stdoutdata, stderrdata) = p.communicate()
  return p.returncode, stdoutdata, stderrdata
  
def SubstDriveToPath(drive, path):
  substcmd = "subst" + " " + drive + " " + path
  return RunCommandWithOutput(substcmd)
  
def UnSubstDriveToPath(drive):
  unsubstcmd = "subst" + " " +drive + " " + "/d"
  RunCommand(unsubstcmd)
  
def SubstDriveToPathF(drive, path):
  UnSubstDriveToPath(drive)
  UnNetuseDriveToPath(drive)
  return SubstDriveToPath(drive, path)

def NetuseDriveToPath(drive, path):
  netusecmd = "net use" + " " + drive + " " + path
  return RunCommandWithOutput(netusecmd)
  
def UnNetuseDriveToPath(drive):
  unnetusecmd = "net use" + " " + drive + " " + "/del"
  RunCommand(unnetusecmd)
  
def NetuseDriveToPathF(drive, path):
  UnSubstDriveToPath(drive)
  UnNetuseDriveToPath(drive)
  return NetuseDriveToPath(drive, path)
  
def AutoSubstorNetuse(path):
  successful = False
  
  if(not os.path.isdir(path) or not os.path.exists(path)):
    print("path is not existed or is not a directory")
    return successful
  
  netuse = False
  if(path.startswith("\\\\")):
    netuse = True
  
  useddrive = ""
  for drive in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
    fulldrive = drive + ":"
    if(netuse):
      (returncode, outdata, errdata) = NetuseDriveToPath(fulldrive, path)
      if(returncode == 0):
        useddrive = fulldrive
        break
    else:
      (returncode,outdata,errdata) = SubstDriveToPath(fulldrive,path)
      if(returncode == 0):
        useddrive = fulldrive
        break
  if(not useddrive == ""):
    successful = True
    
  return successful, useddrive

#(returncode, outdata, errdata) = SubstDriveToPathF("Y:", "C:\\test")
#(returncode1, outdata1, errdata1) =  NetuseDriveToPathF("X:", "\\\\remotemachinenameorip\\shared")

(returncode, drive) = AutoSubstorNetuse("C:\\test")
(returncode, drive) = AutoSubstorNetuse("\\\\remotemachinenameorip\\shared")





