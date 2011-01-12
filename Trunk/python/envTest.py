import os

print (os.environ["TEMP"])

mydir = "c:\\mydir"
os.environ["MYDIR"] = mydir
print (os.environ["MYDIR"])

pathV = os.environ["PATH"]
print (pathV)
os.environ["PATH"]= mydir + ";" + os.environ["PATH"]
print (os.environ["PATH"])