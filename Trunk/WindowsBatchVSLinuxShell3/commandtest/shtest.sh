# test shell

#echo $PATH

ls -la > allfiles.txt

awk '{print $9}' allfiles.txt | grep test | sed s/test/mytest/g

#awk '{print $9}' allfiles.txt > allfiles1.txt
#cat < allfiles1.txt | grep test > allfiles2.txt
#cat < allfiles2.txt | sed s/test/mytest/g 

