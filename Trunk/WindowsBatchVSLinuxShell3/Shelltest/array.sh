
ARRAY=(one two three)
echo ${ARRAY[*]}
unset ARRAY[1]

names=(alice hatter duchess)
for i in "${names[@]}"; do
    echo $i
done

ARRAYNAME[1]=aaa
ARRAYNAME[2]=bbb
echo ${ARRAYNAME[*]} 


values=(39 5 36 12 9 3 2 30 4 18 22 1 28 25)
echo ${#values[@]}

for var in ${values[@]}; do 
  echo $var
done

echo
