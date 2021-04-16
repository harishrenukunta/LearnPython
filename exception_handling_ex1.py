
a = 5
b = 0

try:
    print('Resource opened')
    print(a/b)
    print('Resource closed')
except Exception as e:
    print(e)
finally:
    print('finally -> Resource closed')
