
from numpy import array
from numpy import concatenate

arr1 = array([ 3, 4, 23, 12, 67])
arr2 = array([ 78, 23, 45, 25, 34])

arr1Copy = arr1
arr1[1] = 3
print('arr1:', arr1, "  shallowCopy:", arr1Copy)

arr2DeepCopy = arr2.copy()
print('arr2:', arr2, " Deep Copy:", arr2DeepCopy)
arr2[0] = arr2[0] + 12
print('arr2:', arr2, " Deep Copy:", arr2DeepCopy)
print('Addresses:', 'arr2:', id(arr2), ' arr2DeepCopy:', id(arr2DeepCopy))