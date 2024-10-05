def sort_list(nums):
    x = len(nums)
    for a in range(x):
        for b in range(0, x-a-1):
            if nums[b] > nums[b+1]:
                nums[b], nums[b+1] = nums[b+1], nums[b]
    return nums


print(sort_list([1,5,8,7,4,3,6,9,2]))
