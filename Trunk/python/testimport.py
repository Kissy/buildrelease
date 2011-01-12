
import sys

print ("sys.path is :")
for p in sys.path:
  print (p)

print (type(sys.modules))
print ("sys.modules is:")
for k in sys.modules.keys():
  print ((sys.modules)[k])