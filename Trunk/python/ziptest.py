
import os
import zipfile


filename='c:/test.zip'
curdir="C:/test/"
os.chdir(curdir)

#Create the zip file
tFile = zipfile.ZipFile(filename, 'w')

#Write directory contents to the zip file
files = os.listdir(curdir)
for f in files:
    tFile.write(f)

#List archived files
for f in tFile.namelist():
    print ("Added %s" % f)

#close the zip file
tFile.close()

#whether the file is zip file
print(zipfile.is_zipfile(filename))

#list all file in the zip file
tFile = zipfile.ZipFile(filename, 'r')
for file in tFile.namelist():
    print(file)

#List info for archived file
tinfo=tFile.getinfo("test.log")
print(tinfo.comment)
print(tinfo.compress_size)
print(tinfo.date_time)
print(tinfo.file_size)
print(tinfo.compress_type)
print(tinfo.filename)

#Read zipped file into a buffer
buffer = tFile.read("test.log")
print (buffer)

#close the zip file
tFile.close()


# gzip.GzipFile class
import gzip
underlying_file = open('x.txt.gz', 'rb')
uncompressing_wrapper = gzip.GzipFile(fileobj= underlying_file, mode='rt')
for line in uncompressing_wrapper:
    print (line)
uncompressing_wrapper.close( )
underlying_file.close( )


