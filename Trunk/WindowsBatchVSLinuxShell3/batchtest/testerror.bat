


@echo off

set path="D:\WindowsBatchVSLinuxShell\WindowsBatchVSLinuxShell3\newUnxUtils";path

rem copy source dest | tee.exe copyerror.txt

rem copy source dest 2 > copyerror.txt

rem copy source dest > copyerror.txt

copy source dest > copyerror.txt 2>&1

copy source dest  2>&1 > copyerror.txt


pause
