
import os
def TestFileAttributes():
  # This function is platform indepedent.
  statinfo = os.stat("c:\\python26\\python.exe")
  print statinfo.st_size
  print statinfo.st_atime
  print statinfo.st_mtime
  print statinfo.st_ctime
  #statinfo also include other linux specific information.
  #print statinfo
  
TestFileAttributes()
#27136
#1299820024.28
#1228458748.0
#1228458748.0

import stat
def TestForChangeToWrite(path):
  # This is platform indepedent.
    if not os.access(path,os.W_OK):
        os.chmod(path,stat.S_IWRITE)
        
TestForChangeToWrite("c:\\python26\\python.exe")

##################################################################

import win32api,win32con
def TestWinFileAttributesIfReadonly():
  # This is just for windows.
  fattrs = win32api.GetFileAttributes("c:\\python26\\python.exe")
  #print fattrs
  print bool(fattrs & win32con.FILE_ATTRIBUTE_READONLY) 
 
TestWinFileAttributesIfReadonly()
#False

def TestWinFileAttributesIfHidden():
  # This is just for windows.
  fattrs = win32api.GetFileAttributes("c:\\python26\\python.exe")
  #print fattrs
  print bool(fattrs & win32con.FILE_ATTRIBUTE_HIDDEN) 
 
TestWinFileAttributesIfHidden()
#False

from win32api import GetFileVersionInfo, LOWORD, HIWORD
def get_version_number(filename):
  # This is just for windows.
  info = GetFileVersionInfo(filename, "\\")
  #print info
  ms = info['FileVersionMS']
  ls = info['FileVersionLS']
  print HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
  
get_version_number("C:\\Program Files\\7-Zip\\7z.exe")
#9 20 0 0