import re

def TestSearchAndMatch():
  s1="HelloWorld, I am 30 !"
  
  w1 = "World"
  m1 =  re.search(w1, s1)
  if m1:
    print("Find : %s" % m1.group())
    
  if re.match(w1, s1) == None:
    print("Cannot match")
    
  w2 = "HelloWorld"
  m2 = re.match(w2, s1)
  if m2:
    print("match : %s" % m2.group())

TestSearchAndMatch()
#Find : World
#Cannot match
#match : HelloWorld, I am 30 !

def TestCompile():
  regex = "\d{3}-\d{7}"
  
  regexobject = re.compile(regex)
  print(regexobject.search("AAA 027-4567892").group())
  print(regexobject.search("BBB 021-1234567").group())
  print(regexobject.search("CCC 010-123456"))

TestCompile()
#027-4567892
#021-1234567
#None

def TestIgnorecase():
  print(re.search('world', "hello world !").group())
  print(re.search('World', "hello world !", re.IGNORECASE).group())
  print(re.search('World', "hello world !"))
  
TestIgnorecase()
#world
#world
#None

def TestMatchObject():
  m = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<date>\d{2})", "2010-10-01, i am very happy")
  print(m.group())
  print(m.group(0))
  
  print(m.groups())
  
  print(m.group(1))  
  print(m.groups()[0])
  
  print(m.group(2))  
  print(m.groups()[1])
  
  print(m.group(3))  
  print(m.groups()[2])
  
  print(m.groupdict())
  
  print(m.lastindex)

TestMatchObject()
#2010-10-01
#2010-10-01
#('2010', '10', '01')
#2010
#2010
#10
#10
#01
#01
#{'date': '01', 'year': '2010', 'month': '10'}
#3

def TestReAndMatchObjectMethonds():
  #split findall finditer sub  subn groups  groupindex 
  s1 = "I am working in Microsoft !"
  l = re.split('\s+', s1) # l is list type
  print( l)
  
  s2 = "aa 12 bb 3 cc 45 dd 88 gg 89"
  l2 = re.findall('\d+', s2)
  print(l2)
  
  it = re.finditer('\d+', s2) # it is one iterator type
  for i in it: # i is matchobject type
    print (i.group())
    
  s3 = re.sub('\d+', '200', s2)
  print(s3)
  
TestReAndMatchObjectMethonds()
#['I', 'am', 'working', 'in', 'Microsoft', '!']
#['12', '3', '45', '88', '89']
#12
#3
#45
#88
#89
#aa 200 bb 200 cc 200 dd 200 gg 200

def TestSearch():
  s1 = "bb 3 cc 45 dd 88 gg 89"
  m = re.search('\d+', s1)
  print(m.group())

TestSearch()
#3

