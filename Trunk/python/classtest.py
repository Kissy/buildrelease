

class Class:
    answer = 42
    def __init__(self):
        self.x = 10
    def method(self):
        print( 'Hey a method')
    
print(hasattr(Class, 'answer'))
#True
print(hasattr(Class, 'question'))
#False
print(hasattr(Class(), 'x'))
#True
print(hasattr(Class, 'method'))
#True

print(getattr(Class, 'answer'))
#42
print(getattr(Class, 'question', 'What is six times nine?'))
#'What is six times nine?'
print(getattr(Class(), 'x'))
#10
getattr(Class(),'method')()
#'Hey a method'

class MyClass:
   def method(self):
        print( 'Hey a method')

instance = MyClass()
instance.method()
#'Hey a method'

def new_method(self):
    print( 'New method wins!')


MyClass.method = new_method
instance.method()
#'New method wins!'

del MyClass.method
print(hasattr(MyClass, 'method'))
#False
#instance.method()

instance.y = 20
print(instance.y)
del instance.y


class MyClass2:
    @classmethod
    def a_class_method(cls):
        print ('I was called from class %s' % cls)

    @staticmethod
    def a_static_method():
        print ('I have no idea where I was called from')
        
    def a_static_method2():
        print('i am just called by the class')


instance2 = MyClass2()

MyClass2.a_class_method()
instance2.a_class_method()
# both print 'I was called from class __main__.MyClass2'

MyClass2.a_static_method()
instance2.a_static_method()
# both print 'I have no idea where I was called from'

MyClass2.a_static_method2()
#'i am just called by the class'
#instance2.a_static_method2() # throw exception


