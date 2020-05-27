def add_one(nums):
    carry = 1
    for num in nums:
        sums, carry = (num+carry)%2, (num+carry)//2
        nums[-1] = sums
        if carry == 0:
            return nums
    if carry == 1:
        return [1] + nums
    
