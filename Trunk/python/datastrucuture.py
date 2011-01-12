
def ListFunctions(lists):
  print ("------------------------------------------")
  print (type(lists))
  for item in dir(lists):
    if ( not item.startswith("__")):
      print (item)

#list
l = [1, 2, 3] #or list(1,2,3)
ListFunctions(l)
# tuple
t = (1, 2, 3)
ListFunctions (t)
#set
s = {1, 2, 3} #or set(1,2,3)
ListFunctions(s)
#dictionary
d = {1:'1v', 2:'2v', 3:'3v'} #or dict(1:'1v', 2:'2v', 3:'3v')
ListFunctions(d)
#str
myStr="123" #or str("123")
ListFunctions(myStr)

#file
file = open("test\\file.txt", "r")
ListFunctions(file)
