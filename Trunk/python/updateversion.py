
import os
import os.path
import sys
import re

def UpdateVersionForFile(file, regrexorplaceholder, version):
  f = open(file,"r")
  filestr = f.read()
  f.close()
  
  newfilestr = re.sub(regrexorplaceholder,version, filestr)
  
  if not os.access(file,os.W_OK):
    os.chmod(path,stat.S_IWRITE)
  
  newf = open(file,"w")
  newf.write(newfilestr)
  newf.close()
  
def UpdateVersion(dirorfile, regrexorplaceholder, version):
  if os.path.isfile(dirorfile) and os.path.exists(dirorfile):
     UpdateVersionForFile(dirorfile, regrexorplaceholder, version)
  else:
    print ("update failed")

def usage():
  helpstr = " \n \
  Usage: \n \
     The first parameter need be the file, \n \
     The second parameter need be regrex or placeholder for version, \n \
     The third parameter need be version. \n \
  Examples: \n \
     updateversion.py AssemblyInfo.cs  (\d+\.\d+\.\d+\.\d+)  10.2.0.123456 \n \
     updateversion.py AssemblyInfo.cpp  (\d+\.\d+\.\d+\.\d+)  10.2.0.123456"
  print (helpstr)

if __name__ == "__main__":
  if( not len(sys.argv) == 4):
    print(" The parameters are not correct!")
    usage()
    exit(0)
  UpdateVersion(sys.argv[1], sys.argv[2], sys.argv[3])
  exit(1)
  
  
