class MyIterator():
  def __init__(self, step):
    self.step = step
  
  def __next__(self):
    if self.step==0:
      raise StopIteration
    self.step-=1
    return self.step

  def __iter__(self):
    return self

myI = MyIterator(4)
for e in myI:
  print (e)