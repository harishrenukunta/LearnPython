
from array import *

arr = array('i', [])
no = int(input('Enter the no of elements in an array:'))
for iCounter in range(no):
    val = int(input('Enter value:'))
    arr.append(val)

print('Array you entered:', arr)
searchElement = int(input('Enter value you want to search:'))
iCounter = 0
found = False
for element in arr:
    if element == searchElement:
        found = True
        break
    iCounter+=1

if found == True:
    print('Search Element:', searchElement, ' found in array', ' at', iCounter)
else:
    print('Search Element:', searchElement, ' not found in array')

print('Found element at:', arr.index(searchElement))
