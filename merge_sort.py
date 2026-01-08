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

def selection_sort(nums: list) -> None:
    for i in range(len(nums)):
        smallest = i
        for j in range(i+1, len(nums)):
            if nums[smallest]>nums[j]:
                smallest = j
        nums[smallest], nums[i] = nums[i], nums[smallest]

def insertion_sort(nums: list) -> None:
    for i in range(1, len(nums)):
        for j in range(i,0,-1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break
    # bit slower than selection_sort
    # but if list is almost sorted, insertion sort is effective
    # time complexity : O(N**2)

# merge sort
def merge_sort(L: list) -> None:
    if len(L) <2:
        return L
    mid = len(L)//2
    left= L[:mid]
    right = L[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

def merge(left: list, right: list) -> list:
    merged = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged