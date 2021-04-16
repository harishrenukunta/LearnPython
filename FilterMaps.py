from functools import reduce

lst = [3,2,8, 9, 2]

evens = list(filter(lambda no: no%2 == 0, lst))
doubles = list(map(lambda no: no * 2, lst))
sum = reduce(lambda tot, no: tot + no, lst)
joining = reduce(lambda word, no: str(word) + str(no), lst)

print('List:', lst)
print('Evens from above list:', evens)
print('Doubles from above list:', doubles)
print('Sum of all elements from above list:', sum)
print('Concatenation of nos:', joining)