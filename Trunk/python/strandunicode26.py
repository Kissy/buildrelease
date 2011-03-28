
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
  s = '中国'
  # SyntaxError: (unicode error) 'utf8' codec can't decode bytes in position 0-1
  # us = u'中国'  
  us2 = unicode('中国','gbk')
  
  print (s + ':' + str(type(s))) #中国:<type 'str'>
  # print us
  print (us2 + ':' + str(type(us2))) #中国:<type 'unicode'>
  
  # UnicodeDecodeError: 'ascii' codec can't decode byte 0xd6
  #newstr = s + us2
  
  #UnicodeWarning: Unicode equal comparison failed to convert 
  #both arguments to Unicode - interpreting them as being unequal
  #print 's == us2' + ':' + s == us2
  
  s3 = 'AAA中国'
  print s3 # AAA中国
  
  s4 = unicode('AAA中国','gbk')
  print s4 # AAA中国
  
def TestPrint():
  print 'AAA' + '中国'  # AAA中国
  #print u'AAA' + u'中国' # SyntaxError: (unicode error) 'utf8' codec can't decode bytes in 
  print u'AAA' + unicode('中国','gbk') # AAA中国
  
def TestCodecs():
    import codecs
    
    look  = codecs.lookup("gbk")

    a = unicode("北京",'gbk')

    print len(a), a, type(a) #2 北京 <type 'unicode'>

    b = look.encode(a)
    print b[1], b[0], type(b[0]) #2 北京 <type 'str'>
    

if __name__ == '__main__':
    TestisStrOrUnicdeOrString()
    TestChinese()
    TestPrint()
    TestCodecs()
