
val1=12 val2=5 
result1=val*val2 
echo $result1 

a=2
c=5
let b=$a*$c
echo $b

declare -i val3=12 val4=5
declare -i result2
result2=val3*val4
echo $result2


echo $[365*24] 
echo $[1-5*6+20]
echo $(( (3 > 2) || (4 <= 1) )) 




