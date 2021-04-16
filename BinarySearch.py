
pos = -1
def binary_search(lst, no):
    low_indx = 0
    up_indx = len(lst) - 1
    while low_indx <= up_indx:
        mid_indx = (low_indx + up_indx) // 2
        if(lst[mid_indx] == no):
            globals()['pos'] = mid_indx
            return True
        else:
            if lst[mid_indx] < no:
                low_indx = mid_indx + 1
            else:
                up_indx = mid_indx

    return False


lst = [23, 34, 65, 89, 82, 454, 2]
sorted_lst = sorted(lst)
print('orig:{} sorted_lst:{}'.format(lst, sorted_lst))
search_no = 23
found = binary_search(sorted_lst, search_no)
if found:
    print('Element {} found at position {}'.format(search_no, pos+1))
else:
    print('Element {} not found'.format(search_no))