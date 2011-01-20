
import random
import string
import time

# strong.high = 3  #random for the whole passwd
#storng.middle = 2  # include one special sign
#strong.ow = 1  # just include characters or digits

def mkpassByRandom(size=8, strong = 2):
    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    chars.extend([i for i in '\'"!@#$%&*()-_=+[{}]~^,<.>;:/?'])
    
    passwd = ''
    strong = int(strong)
    
    if (strong <= 1) :
     for i in range(size):
       passwd += chars[random.randint(0,len(string.ascii_letters + string.digits) - 1)]
       random.seed = int(time.time())
    elif(strong == 2):
       newpasswd = ''
       for i in range(size - 1):
         newpasswd +=chars[random.randint(0,len(string.ascii_letters + string.digits) - 1)]
         random.seed = int(time.time())
       newpasswd += chars[random.randint(len(string.ascii_letters + string.digits) , len(chars) - 1)]
       ll = [ch for ch in newpasswd]
       random.shuffle(ll)
       for l in ll:
         passwd += l
    elif(strong >=3):
      for i in range(size):
        passwd += chars[random.randint(0,  len(chars) - 1)]
        random.seed = int(time.time())
        random.shuffle(chars)
    else:
      pass
     
    return passwd
  
def rule1(ch):
    rulesdict = { 'o': 0, 'i':'!', 'b':8, 'p':'P', 'm':'M'}
    newch = ch
    
    if ch in rulesdict.keys():
      newch = rulesdict[ch]
    return newch

def rule2(ch):
  if(ch.isupper()):
    return ch.lower()
  elif(ch.islower()):
    return ch.upper()
  return ch

def mkpassByRules(passwd, *rules ):
  if (passwd == "" or len(rules) == 0):
    return passwd
  
  newpasswd = ""
  for c in passwd:
    r = random.randint(0, len(rules) - 1)
    ch = (rules[r])(c)
    newpasswd += str(ch)

  return newpasswd


def mkpass(size = 8, strong = 2, initpasswd = ""):
  if ( not initpasswd == ""):
    return mkpassByRules(initpasswd, rule1, rule2)
  else:
    return mkpassByRandom(size,strong)

print( mkpass(initpasswd = "Password123"))
print( mkpass(strong = 1))
print( mkpass(strong = 2))
print( mkpass(strong = 3))


 