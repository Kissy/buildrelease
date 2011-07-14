
import time

ISOTIMEFORMAT='%Y-%m-%d %X'

# seconds from 1970.01.01 00:00:00
t = time.time()
print (t)
print time.strftime(ISOTIMEFORMAT,time.localtime(t))
#1310623143.12
#2011-07-14 13:59:03

(year,mon,day,hour,min,sec,wday,yday,isdst) = time.localtime()
print (year)
print (time.strftime(ISOTIMEFORMAT, time.localtime()))
#2011
#2011-07-14 13:59:03