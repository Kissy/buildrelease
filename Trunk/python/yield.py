
def TestIterator():
  for e in [2, 4, 8, 16]  :
   print(e)
  for c in 'ABCDEFG' :
    print (c)
    
  #use list iterator
  for line in open("test.txt").readlines():
    print (line )
    
  #use file iterator, and it is better. not read all data into memory
  for line in open("test.txt"):   
    print (line )

#TestIterator()

class MyIterator():
  def __init__(self, step):
    self.step = step
  
  def next(self):
    if self.step==0:
      raise StopIteration
    self.step-=1
    return self.step
  
  def __iter__(self):
    return self

def TestMyIterator():
    myI = MyIterator(4)
    print (myI.next())
    for e in myI:
      print (e)
      
def TestGenerator(l):
  for e in l:
   print ("before yield:" + str(e))
   yield e
   print ("after yield:" + str(e))
   
#for el in TestGenerator([6,7,8,9]):
  #print (el)
  #break
    
def Generator2(l):
  for e in l:
    print ("before yield:" + str(e))
    enew = yield e
    print ("after yield:" + str(enew))

def TestGenerator2():
    it = TestGenerator2([6,7,8,9])
    for i in range(6,10):
      if i == 8 :
        element = it.send(800)
      else:
        element = it.next()
      print(element)

def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

def TestCounter():
    co = counter(10)
    for e in co:
      print (e)
      if(e == 2):
        co.send(8)
  
TestCounter()
