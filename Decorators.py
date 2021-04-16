
def div(a,b):
    return a/b

def smar_div(func):
   def inner(a,b):
       if a < b:
           a, b = b, a
       return func(a,b)
   return inner

div = smar_div(div)
print('Div:', div(5, 10))