import subprocess
import datetime
import time

def TestPopen():
  import subprocess
  p=subprocess.Popen("dir",shell=True)
  for i in range(250) :
    print ("other things")

def TestWait():
  import subprocess
  import datetime
  print (datetime.datetime.now())
  p=subprocess.Popen("sleep 10",shell=True)
  p.wait()
  print (p.returncode)
  print (datetime.datetime.now())
 
def TestPoll():
  import subprocess
  import datetime
  import time
  print (datetime.datetime.now())
  p=subprocess.Popen("sleep 10",shell=True)
  t = 1
  while(t <= 5):
    time.sleep(1)
    p.poll()
    print (p.returncode)
    t+=1
  print (datetime.datetime.now())


def TestCommunicate():
  import subprocess
  p=subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (stdoutdata, stderrdata) = p.communicate()
  print (p.stdout.read())
  print (p.returncode)


def TestKillAndTerminate():
    p=subprocess.Popen("notepad.exe")
    t = 1
    while(t <= 5):
      time.sleep(1)
      t +=1
    p.kill()
    #p.terminate()
    print ("new process was killed")
    
def TestCall():
  retcode = subprocess.call("c:\\test.bat")
  print (retcode)
  
def TestGetOutput():
  outp = subprocess.getoutput("ls -la")
  print (outp)

def TestGetStatusOutput():
  (status, outp) = subprocess.getstatusoutput('ls -la')
  print (status)
  print (outp)
  
  
if __name__=="__main__" :
  #TestPopen()
  #TestWait()
  #TestPoll()
  TestCommunicate()
  #TestKillAndTerminate()
  #TestCall()
  #TestOutPut()
  #TestGetStatusOutput()