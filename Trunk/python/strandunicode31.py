
# -*- coding: gbk -*-

def TestisStrOrUnicdeOrString():
  bs = b'Hello'
  ustr = 'abc'
  print (isinstance(bs, str))  #False
  print (isinstance(bs,bytes)) #True
  print (isinstance(ustr,str)) #True
  print (isinstance(ustr, bytes)) #False
  print (isinstance(bs,(bytes,str))) #True


def TestChinese():
  us = '�й�'
  bs = b'AAA'
  bs2 = bytes('�й�','gbk')
  
  print (us + ':' + str(type(us))) #�й�:<class 'str'>
  print (bs) #AAA
  print (bs2) # b'\xd6\xd0\xb9\xfa'
  print (':' + str(type(bs2))) #:<class 'bytes'>
  print (bs2.decode('gbk')) #�й�
  
  # TypeError: Can't convert 'bytes' object to str implicitly
  #newstr = us + bs2
  
  print ('us == bs2' + ':' + str(us == bs2)) #us == bs2:False
  
  s3 = 'AAA�й�'
  print (s3) # AAA�й�
  
  s4 = bytes('AAA�й�','gbk')
  print (s4) # b'AAA\xd6\xd0\xb9\xfa'
  
def TestPrint():
  print ('AAA' + '�й�')  # AAA�й�
  #print (b'AAA' + b'�й�') #  # SyntaxError: bytes can only contain ASCII literal characters.
  #print ('AAA' + bytes('�й�','gbk')) # TypeError: Can't convert 'bytes' object to str implicitly
  
def TestCodecs():
    import codecs
    
    look  = codecs.lookup("gbk")

    a = bytes("����",'gbk')

    print (len(a), a, type(a)) #4 b'\xb1\xb1\xbe\xa9' <class 'bytes'>

    b = look.decode(a)
    print (b[1], b[0], type(b[0])) #4 ���� <class 'str'>
    

if __name__ == '__main__':
    TestisStrOrUnicdeOrString()
    TestChinese()
    TestPrint()
    TestCodecs()
