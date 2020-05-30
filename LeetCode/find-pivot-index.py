def pivot_index(nums):
    if len(nums) < 3: return -1
    sum_nums = sum(nums)
    sum_curr = 0
    for i in range(1,len(nums)):
        sum_curr += nums[i-1]
        if sum_curr == sum_nums - sum_curr - nums[i]:
            return i
    return -1
        
        
