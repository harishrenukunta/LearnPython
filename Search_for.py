
lst = [56, 21, 234, 567, 23, 12]

def search(lst, no):
    for n in lst:
        if n == no:
            return True
    return False

no = 234
if search(lst, no):
    print('Found no:{}'.format(no))
else:
    print('no:{} not found'.format(no))

