
def load_endings(string_list):
    endings = set()
    for f in open(string_list).readlines():
       endings.add(f.strip())
    return endings
    

def process_files(string_list):
    file_endings = load_endings(string_list)
    for ending in file_endings:
     path = 'D:\BuildForge\MB_Opus\MB_Opus_01132011.220036\bin\win32\adlmint_libFNP.dll'
     if path.endswith(ending):
        print (ending)
        
        
def RemoveReadonly():
  import os
  import stat
  os.chmod( "c:\\test\\buildid.txt", stat.S_IWRITE )

RemoveReadonly()
#process_files("c:\\test\\keepfile.txt")