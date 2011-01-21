@echo off

echo get the value from one txt file
rem the num.txt file only contains one line "001".

echo work well
set /p num=<num.txt
echo %num%

echo doesn't work
set num=<num.txt
echo %num%
type num.txt | set num=
echo %num%
type num.txt | set /p num=
echo %num%
set num=(`print num.txt`)
echo %num%

echo get value from command
echo some command work well, such as %time%, %date% ...
set bbb=%time% 
echo %bbb%
set aaa=%date%
echo %aaa%

echo general command doesn't work
set ccc=('time /t')
echo %ccc%

echo one solution is to output the result to txt and then input it
time /t > ddd.txt
set /p ddd=<ddd.txt
echo %ddd%

echo specially,in for clause, ('time /t') is as one command.
echo and if also use setlocal enabledelayedexpansion, the way also can implement get value from command.
setlocal enabledelayedexpansion
for /f %%i in ('time /t') do (
    echo %%i
    set ti=%%i
    echo !ti!
)

pause