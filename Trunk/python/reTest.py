import re

oldline = 'dir=c:\\test\\2010'
str1 = 'Hello\n' + oldline +'\nHow are you!'
print str1
print '------------------------------------'

newline = 'dir=c:\\test\\2011'

reobj = re.compile('^(dir=)(.*)$',re.M)  
newStr1 = reobj.sub(newline, str1 )
print newStr1
print '------------------------------------'

newdir = 'c:\\test\\2011'
def f(m):
  return m.group(1) + newdir  
newNewStr1 = reobj.sub(f, str1 )
print newNewStr1
print '------------------------------------'