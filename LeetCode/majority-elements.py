def majority-element(nums):
    if not nums: return nums
    n = len(nums)
    if n % 2:
        threshold_count = n // 2 + 1
    else:
        threshold_count =  n // 2
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    for num in d:
        if d[num] >= threshold_count:
            print(num)
    return None
    
