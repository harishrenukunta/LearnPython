import sys
def factorialRecursion(no):
    if(no == 1):
        return 1
    return no * factorialRecursion(no-1)

print('Recursion limit:', sys.getrecursionlimit())
number = int(input('Enter no to find factorial:'))
print('Factorial of given no:', factorialRecursion(number))