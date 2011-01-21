@echo off 

echo 调用前 

echo 调用子过程 
call :sub

echo 调用后 
Goto end

:sub 
echo 子过程调用中
goto :eof 

:end
echo 退出
Pause 
exit
