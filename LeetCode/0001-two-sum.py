def twoSum(nums, target):
    d = {}
    for i,num in enumerate(nums):
        need = target - num
        if need in d:
            return (d[need], i)
        d[num] = i
    return (-1, -1)
