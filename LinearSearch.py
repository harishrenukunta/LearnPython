
pos = -1
def search(lst, n):
    iCounter = 0
    while iCounter < len(lst):
        if lst[iCounter] == n:
            globals()['pos'] = iCounter
            return True
        iCounter += 1
    return False

lst = [6, 3, 2, 8, 10]

n= 2
if search(lst, n):
    print('Found no:{} at position:{}'.format(n, pos+1))
else:
    print('No:{} Not found'.format(n))