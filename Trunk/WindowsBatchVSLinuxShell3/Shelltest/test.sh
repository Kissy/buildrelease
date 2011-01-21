
MgDevRoot=$1

PHPAndApacheInstallDir=$MgDevRoot/Web

echo $PHPAndApacheInstallDir
echo $PHPAndApacheInstallDir | sed 's/\\/\//g' > temp.txt
PHPAndApacheInstallDir=`cat temp.txt`
rm -f temp.txt
echo $PHPAndApacheInstallDir


echo $PHPAndApacheInstallDir | sed 's#/#\\\\#g' > temp.txt
PHPAndApacheInstallDir=`cat temp.txt`
rm -f temp.txt
echo $PHPAndApacheInstallDir