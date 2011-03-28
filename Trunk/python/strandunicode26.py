
# -*- coding: utf-8 -*-

def TestisStrOrUnicdeOrString():
  s = 'abc'
  ustr = u'Hello'
  print isinstance(s, str)  #True
  print isinstance(s,unicode) #False
  print isinstance(ustr,str) #False
  print isinstance(ustr, unicode) #True
  print isinstance(s,basestring) #True
  print isinstance(ustr,unicode) #True


def TestChinese():
  # for the below chinese, must add '# -*- coding: utf-8 -*-' in first or second line of this file 
  s = '�й�'
  # SyntaxError: (unicode error) 'utf8' codec can't decode bytes in position 0-1
  # us = u'�й�'  
  us2 = unicode('�й�','gbk')
  
  print (s + ':' + str(type(s))) #�й�:<type 'str'>
  # print us
  print (us2 + ':' + str(type(us2))) #�й�:<type 'unicode'>
  
  # UnicodeDecodeError: 'ascii' codec can't decode byte 0xd6
  #newstr = s + us2
  
  #UnicodeWarning: Unicode equal comparison failed to convert 
  #both arguments to Unicode - interpreting them as being unequal
  #print 's == us2' + ':' + s == us2
  
  s3 = 'AAA�й�'
  print s3 # AAA�й�
  
  s4 = unicode('AAA�й�','gbk')
  print s4 # AAA�й�
  
def TestPrint():
  print 'AAA' + '�й�'  # AAA�й�
  #print u'AAA' + u'�й�' # SyntaxError: (unicode error) 'utf8' codec can't decode bytes in 
  print u'AAA' + unicode('�й�','gbk') # AAA�й�
  
def TestCodecs():
    import codecs
    
    look  = codecs.lookup("gbk")

    a = unicode("����",'gbk')

    print len(a), a, type(a) #2 ���� <type 'unicode'>

    b = look.encode(a)
    print b[1], b[0], type(b[0]) #2 ���� <type 'str'>
    

if __name__ == '__main__':
    TestisStrOrUnicdeOrString()
    TestChinese()
    TestPrint()
    TestCodecs()
