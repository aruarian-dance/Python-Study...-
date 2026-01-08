def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping==True:
        swapping=False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                tmp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp
                swapping=True
        end -= 1
    return nums