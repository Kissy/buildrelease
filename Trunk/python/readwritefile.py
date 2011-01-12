
outPath = "text.txt"
inPath = outPath
print('---------------------------------')
#Open a file for writing
file = open(outPath, 'w')
if file:
    file.write('hello\ntom\n')
    file.writelines('bye!')
    file.close()
else:
    print ("Error Opening File.")
    
print('---------------------------------')
#Open a file for reading
file = open(inPath, 'r')
if file:
    print(file.read())
    #print(file.readlines())
    file.close()
else:
    print ("Error Opening File.")

print('---------------------------------')
# read line from file
import linecache
filePath = "text.txt"

print (linecache.getline(filePath, 1))
print (linecache.getline(filePath, 3))
linecache.clearcache()

print('---------------------------------')
# read word from file
filePath = "input.txt"
wordList = []
wordCount = 0

#Read lines into a list
file = open(filePath, 'rU')
for line in file:
    for word in line.split():
        wordList.append(word)
        wordCount += 1
print (wordList)
print ("Total words = %d" % wordCount)

print('---------------------------------')
# count line of file
filePath = "input.txt"
lineCount = len(open(filePath, 'rU').readlines())
print ("File %s has %d lines." % (filePath,lineCount))
