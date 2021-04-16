
def bubble_sort(nums):
    for rowNo in range(len(nums) - 1, 0, -1):
        for no_indx in range(rowNo):
            if(nums[no_indx] > nums[no_indx + 1]):
                temp = nums[no_indx]
                nums[no_indx] = nums[no_indx + 1]
                nums[no_indx + 1] = temp
    return nums;

nums = [45, 23, 18, 1, 5, 6, 100, 12]
print('nums:{}'.format(nums))
bubble_sort(nums)
print('sorted:{}'.format(nums))


