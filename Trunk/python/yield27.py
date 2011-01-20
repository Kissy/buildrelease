
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

#myI = MyIterator(4)
#for e in myI:
  #print e

  
def TestGenerator(l):
  for e in l:
    print ("before yield:" + str(e))
    enew = yield e
    print ("after yield:" + str(enew))
  
it = TestGenerator([6,7,8,9])
for i in range(6,10):
  if i == 8 :
    element = it.send(800)
  else:
    element = it.next()
  print(element)

