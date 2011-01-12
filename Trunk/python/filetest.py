
f = open("hello.txt")
try:
 for line in f:
    print(line)
finally:
	f.close()
		
f2 = open("hello.txt", w)
try:
    f2.writeline("hello")
    f2.writeline("jason")
finally:
f2.close()