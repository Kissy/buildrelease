
def TestTryException():
    try:
        f = open('myfile.txt')
        s = f.readline()
        f.close()
        i = int(s.strip())
    except IOError as ioerror :
        print (ioerror)
    except ValueError as valueerror:
        print (valueerror)
    except:
        print ("Unexpected error")
    else:
       print (i)
    finally:
       print ("always running")
       
#TestTryException()
       
       
class MyError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
         
def TestMyException():
  try:
     raise MyError(2*2)
  except MyError as e:
    print (e)
    
#TestMyException()
    
def TestWith():
  with open("myfile.txt") as f:
     for line in f:
         print (line)
  f.readline() #f is cleanup here, here will get ValueError exception
   
TestWith()

class controlled_execution(object):
    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        try:
            f = open(self.filename, 'r')
            content = f.read()
            return content
        except IOError  as e:
            print (e)

    def __exit__(self, type, value, traceback):
        if self.f:
            print ('type:%s, value:%s, traceback:%s' % (str(type), str(value), str(traceback)))
            self.f.close()

def TestWithAndException():
    with controlled_execution("myfile.txt") as thing:
        if thing:
            print(thing)

#TestWithAndException()


