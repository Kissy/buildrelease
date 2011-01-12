import os
from os.path import join,splitext
all_files=[]
exts=('.avi','.rmvb','.mp3','.bmp')
to_write_file='J:\\out.txt'
base_path='J:\\Desperate.hoursewives'
for root,dirs,files in os.walk(base_path):
	print (dirs)
	for name in files:
		print (name)
		file_path=join(root,name)
		if splitext(file_path)[1] in exts:
			all_files.append(file_path)
if len(all_files)>0:
	fs=open(to_write_file,'w')
	fs.write('\n'.join(all_files))
	fs.close()
	print ("successfully writes %d lines" % len(all_files))
else:
	print ('soory,these is no files found.')

