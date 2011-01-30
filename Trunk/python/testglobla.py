def f1():
    v1 = 'local'
    f2()
    print (v1)

def f2():
   print(v1)

v1 = "Value1"
f1()
#Value1
#local

def f3():
  def f4():
    print (v3)
  v3 = "Value3#"
  print(v3)
  f4()

v3 = "Value3"
f3()
#Value3#
#Value3#


def f5():
  v51 = 100
  v53 = v52
  v53.append(100)
  print( v51)
  print( v53)
  
v51 = 10
v52 = [10]
f5()
print(v51)
print(v52)
#100
#[10, 100]
#10
#[10, 100]

def f6():
  global v6 
  print(v6)
  v6 = "local"
  print(v6)
  
v6 = "global"
f6()
print(v6)
#global
#local
#local

def f7(right):
  if(right):
     result = True
  else:
     result = False
  print (result)
  
  try:
    v7 = "Value7"
  except:
    pass
  print(v7)
  
f7(False)
#False
#Value7


