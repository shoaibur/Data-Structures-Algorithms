def missingNumber(nums):
    # Sol 1. Using hash map
    # d = {}
    # for num in nums:
    #     d[num] = 1
    # for num in range(len(nums)+1):
    #     if num not in d:
    #         return num
    # return -1
    # Sol 2. Summation of series
    n = len(nums)
    series_sum = n*(n+1) // 2
    nums_sum = sum(nums)
    return series_sum - nums_sum
