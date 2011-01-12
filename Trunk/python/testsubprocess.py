def TestCommunicate():
  import subprocess
  cmd = "dir"
  p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (stdoutdata, stderrdata) = p.communicate()
  
  if p.returncode != 0:
        print (cmd + "error !")
  #defaultly the return stdoutdata is bytes, need convert to str and utf8
  for r in str(stdoutdata,encoding='utf8' ).split("\n"):
    print (r)
  print (p.returncode)


def TestCommunicate2():
  import subprocess
  cmd = "dir"
  #universal_newlines=True, it means by text way to open stdout and stderr
  p = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  curline = p.stdout.readline()

  while(curline != ""):
        print (curline)
        curline = p.stdout.readline()
  p.wait()
  print (p.returncode)
  
def TestGetOutput():
  import subprocess
  outp = subprocess.getoutput("dir")
  print (outp)

TestGetOutput()
#TestCommunicate2()