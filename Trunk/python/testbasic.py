
def TestCopy():
    a = 10
    b = a
    a =20
    print (b) #b still is 10
    
def TestRef():
    a=[1,2,3,4]
    b=a   #b is a reference to a
    print (b is a) # True
    b[2] = -100 #change an element in b
    print (a) # a also changed to [1,2,-100,4]

def TestShallowCopy():
    a = [ 1, 2, [3,4] ]
    b = list(a) # create a shallow copy of a
    print (b is a) #False
    b.append(100) #append element to b
    print (b)
    print (a) # a is unchanged
    b[2][0] = -100 # modify an element inside b
    print (b)
    print (a)  # a is changed 
    
def TestDeepCopy():
  import copy
  a = [1, 2, [3, 4]]
  b = copy.deepcopy(a)
  b[2][0] = -100
  print (b)  # b is changed
  print (a)  # a is unchanged
  
def TestGarbageCollection():
  import sys
  print(sys.getrefcount(37))
  a = 37 # Creates an object with value 37
  print(sys.getrefcount(37))
  b = a # Increases reference count on 37
  print(sys.getrefcount(37))
  c = []
  c.append(b) # Increases reference count on 37
  print(sys.getrefcount(37))
  del a # Decrease reference count of 37
  print(sys.getrefcount(37))
  b = 42 # Decrease reference count of 37
  print(sys.getrefcount(37))
  c[0] = 2.0 # Decrease reference count of 37
  print(sys.getrefcount(37)) 
  
TestGarbageCollection()


