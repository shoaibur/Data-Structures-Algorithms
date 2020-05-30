def max_sum_subarray(nums):
    if len(nums) <= 1: return nums
    max_sum = nums[0]
    summ = 0
    for num in nums[1:]:
        summ = max(summ, summ+num)
        max_sum = max(max_sum, summ)
    return max_sum
