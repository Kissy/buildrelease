

#list to another list
numbers = [1,2,3,4,5]
squares = [number*number for number in numbers]
print(squares)
# [1,4,9,16,25]

numbers_under_4 = [number for number in numbers if number < 4]
print(numbers_under_4)
# [1,2,3]

squares_under_4 = [number*number for number in numbers if number < 4]
print(squares_under_4)
# [1,4,9]

#list and for, not foreach
strings = ['a', 'b', 'c', 'd', 'e']
for index, string in enumerate(strings):
    print (index, string)
# '0 a 1 b 2 c 3 d 4 e'

#list any and all
numbers2 = [1,2,3,4,5,6,7,8,9]
if all(number < 10 for number in numbers2):
    print ('Success!')
# 'Success!'
numbers3 = [1,10,100,1000,10000]
if any(number < 10 for number in numbers3):
    print ('Success!')
#  'Success!'

#mutiply list
mat = [[1,2,3],[4,5,6]]
for i in [0,1,2]:
    for row in mat:
        print(row[i],end=" ")
    print()
#1 4 
#2 5 
#3 6
print(list(zip(*mat)))
#[(1, 4), (2, 5), (3, 6)]

#list union by set
numbers4 = [1,2,3,3,4,1]
print(set(numbers4))
#{1,2,3,4}
if len(numbers4) == len(set(numbers4)):
    print ('List is unique!')


#dictionary
keyGenDict={1:'blue',4:'fast',2:'test'}
print (keyGenDict.keys())
print (keyGenDict.values())
print (keyGenDict.items())

keys=list(keyGenDict.keys())
keys.sort()
for key in keys:
    print(keyGenDict[key])
    
for key, value in keyGenDict.items():
    print(key,value)
