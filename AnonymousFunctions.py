from array import *
add = lambda a,b : a+b
square = lambda a : a*a
minus = lambda a,b: a - b
multiply = lambda a, b: a * b

print('Enter two numbers:')
nos = array('i', [])
for iCounter in range(2):
    nos.append(int(input('Enter number:')))


print('Add:', add(nos[0], nos[1]))
print('Square:', square(nos[0]))
print('Product:', multiply(nos[0], nos[1]))
print('Substract:', minus(nos[0], nos[1]))