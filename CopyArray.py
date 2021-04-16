
from array import *
arr = array('i', [45, 23, 21, 34, 67])
dest = array(arr.typecode, [])
for ele in arr:
    dest.append(ele + 2)

print("Src:", arr)
print("Dest:", dest)
