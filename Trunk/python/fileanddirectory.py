

import os

# tree c:\test /f
#C:\TEST
#│  test.log
#│
#├─test2
#│      test2.log
#│
#└─test3

tree = os.walk('C:/test')
for directoryItem in tree:
    directory=directoryItem[0]
    subDirectories=directoryItem[1]
    filesInDirectory=directoryItem[2]    
    print('-----------------')
    print('the directory is :', directory)
    print('the sub directories are : ', subDirectories)
    print('the files are :', filesInDirectory)

#-----------------
#the directory is : C:/test
#the sub directories are :  ['test2', 'test3']
#the files are : ['test.log']
#-----------------
#the directory is : C:/test\test2
#the sub directories are :  []
#the files are : ['test2.log']
#-----------------
#the directory is : C:/test\test3
#the sub directories are :  []
#the files are : []

