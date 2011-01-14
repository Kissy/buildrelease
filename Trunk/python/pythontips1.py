
print("hello %s : %s" % ("AAA", "you are so nice"))

names = ['jianpx', 'yue']   
ages = [23, 40]   
m = dict(zip(names,ages)) 
print (m)

fruits = ['apple', 'banana']   
result = ''.join(fruits) 

d = {1:"v1", 2:"v2"}
if 1 in d.keys():
  print("d dict has the key 1")
  

l = [1,2,2,3]
l2 = set(l)
print(l2)

l = [1,3, 4]
for index, value in enumerate(l):
    print ('%d, %d' % (index, value))
    
names = 'jianpx, yy, mm, , kk'
result = [name for name in names.split(',') if name.strip()]

add = lambda x,y : x + y
print(add(1,2))

a=[0,1,2,3,4,5,6,7]
b=filter(None, a)
print (list(b))
c=filter(lambda x : x %2 == 0, a)
print(list(c))
d=filter(lambda x:x>5, a)
print (list(d))
#[1, 2, 3, 4, 5, 6, 7]
#[0, 2, 4, 6]
#[6, 7]

import functools
a = [1,2,3,4,5]
s = functools.reduce(lambda x,y:x+y,a)
print(s)
#15

a=[0,1,2,3,4,5,6,7]
m = map(lambda x:x+3, a)
print(list(m))
#[3, 4, 5, 6, 7, 8, 9, 10]

strings = ['a', 'b', 'c', 'd', 'e']
for index in range(len(strings)):
    print (index)
# prints '0 1 2 3 4'

numbers = [1,2,3,4,5,6,7,8,9]
if all(number < 10 for number in numbers):
    print ("Success!")
# Output: 'Success!'

numbers = [1,10,100,1000,10000]
if any(number < 0 for number in numbers):
    print ('Success!')
else:
    print('Fail!')
 # Output: 'Fail!'
 
numbers = [1,2,3,3,4,1]
if len(numbers) == len(set(numbers)):
    print ('List is unique!')
# In this case, doesn't print anything

emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
email_at_dotcom = dict( [name, '.com' in email] for name, email in emails.items() )
print(email_at_dotcom)
# email_at_dotcom now is {'Dick': True, 'Jane': True, 'Stou': False}

test = True
# test = False
result = test and 'Test is True' or 'Test is False'
print(result)
# result is now 'Test is True'

string = 'Hi there' # True example
# string = 'Good bye' # False example
if string.find('Hi') != -1:
    print ("Success!")

string = 'Hi there' # True example
# string = 'Good bye' # False example
if 'Hi' in string:
    print ('Success!')
    

numbers = (1,2,3,4,5) # Since we're going for efficiency, I'm using a tuple instead of a list ;)
squares_under_10 = (number*number for number in numbers if number*number < 10)
# squares_under_10 is now a generator object, from which each successive value can be gotten by calling .next()
for square in squares_under_10:
    print ( square)
    # prints '1 4 9'
    
def TestDefaultArgs(a = 1, b =2):
  aa = a
  bb = b
  print (repr(aa) + " " + str(bb))

TestDefaultArgs(3)
TestDefaultArgs(4,3)
TestDefaultArgs(5)

def f2(a, L=[]):
    L.append(a)
    return L
print(f2(1))
print(f2(2))
print(f2(3))
def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f3(1))
print(f3(2))
print(f3(3))
# the result will be
#[1]
#[1, 2]
#[1, 2, 3]
#[1]
#[2]
#[3]

from copy import deepcopy
def resetDefaults(f):
    defaults = f.__defaults__
    def resetter(*args, **kwds):
        f.__defaults__ = deepcopy(defaults)
        return f(*args, **kwds)
                    
    resetter.__name__ = f.__name__
    return resetter
                            
@resetDefaults # This is how you apply a decorator 
def TestDefaultCorrect(item, stuff = []): 
     stuff.append(item) 
     print (stuff)

TestDefaultCorrect(1)
# prints '[1]' 
TestDefaultCorrect(2)
# prints '[2]', as expected


def decorator1(func):
    return lambda: func() + 1

def decorator2(func):
    def print_func(): 
        print (func())
    return print_func

@decorator2
@decorator1
def function():
    return 41

# to cal functions(), it is equal to call decorator2(decorator1(function))

function()
# prints '42'


class Class:
    answer = 42

getattr(Class, 'answer')
# returns 42
getattr(Class, 'question', 'What is six times nine?')
# returns 'What is six times nine?'
#getattr(Class, 'question')
# raises AttributeError

class Class: 
   def method(self): 
       print ('Hey a method' )
       
instance = Class() 
instance.method() 
# prints 'Hey a method' 

def new_method(self):
    print ('New method wins!')
    
Class.method = new_method
instance.method()
# prints 'New method wins!'



class Class:
    @classmethod
    def a_class_method(cls): 
       print ('I was called from class %s' % cls)

    @staticmethod
    def a_static_method(): 
        print ('I have no idea where I was called from')
        
    def another_static_method():
         print ('I have no idea where I was called from2')

    def an_instance_method(self):
        print ('I was called from the instance %s' % self)

instance = Class()

Class.a_class_method()
instance.a_class_method()
# both print 'I was called from class __main__.Class'

Class.a_static_method()
instance.a_static_method()
# both print 'I have no idea where I was called from'

Class.another_static_method()
# both print 'I have no idea where I was called from2'
#instance.another_static_method()
#TypeError: another_static_method() takes no arguments (1 given)

#Class.an_instance_method()
# TypeError: an_instance_method() takes exactly 1 positional argument (0 given)
instance.an_instance_method()
# prints something like 'I was called from the instance <__main__.Class instance at 0x2e80d0>'
