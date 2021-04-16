
def selection_sort(nums):
    for rowNo in range(len(nums)-2):
        for jCounter in range(rowNo + 1, len(nums) - 1):
            if(nums[rowNo] > nums[jCounter]):
                temp = nums[rowNo]
                nums[rowNo] = nums[jCounter]
                nums[jCounter] = temp


list_of_values = [34, 23, 12, 45, 56, 890]
print('list of values:{}'.format(list_of_values))
selection_sort(list_of_values)
print('sorted values:{}'.format(list_of_values))