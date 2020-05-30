# Brute-force: O(n^2), O(1)
# Sorted and two pointers: O(n log n), O(1)
# Hash maps: O(n), O(n)

# Two pinters
def two_sum(nums, target):
    nums.sort()
    i, j = 0, len(nums)-1
    while i < j:
        summ = nums[i] + nums[j]
        if summ == target:
            return (i, j)
        if summ > target:
            j -= 1
        else:
            i += 1
    return (-1,-1)
    
# Hash maps
def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in d:
            return (d[need], i)
        else:
            d[num] = i
    return (-1, -1)
    
