
class Calculator:

   @staticmethod
   def sum(a=None, b=None, c=None):
       if a!=None and b!=None and c!=None:
           return a + b + c
       elif a!=None and b!=None:
           return a + b
       else:
           return a

print('Sum of 5 + 6 + 10:{}'.format(Calculator.sum(5, 6, 10)))
print('Sum of 6 + 7:{}'.format(Calculator.sum(6, 7)))
