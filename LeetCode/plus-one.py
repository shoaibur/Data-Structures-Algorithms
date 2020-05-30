def plus_one(nums):
    carry = 1
    for i in range(len(nums)-1, -1, -1):
        num = nums[i] + carry
        summ, carry = num % 10, num // 10
        nums[i] = summ
        if carry == 0:
            return nums
    if carry == 1:
        return [1] + nums
        
# Recursive solution
def plus_one(nums):
    if nums[-1] == 9: return [1, 0]
    if nums[-1] < 9:
        nums[-1] += 1
        return nums
    return plus_one(nums[:-1]) + [0]
    
