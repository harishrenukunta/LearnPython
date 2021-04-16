
def greet():
    print('Hello World')

def greetWithName(name):
    print('Hello ', name)

def add(x, y):
    return x+y

def add_sub(x, y):
    return x+y, x-y

greet()
greetWithName('Harish')
print('Add(4,3):', add(4, 3))
print('Add Sub(5,2):', add_sub(5, 1))