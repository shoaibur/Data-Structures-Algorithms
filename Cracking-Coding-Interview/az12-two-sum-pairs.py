# Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.
# Conditions:
# You will pick exactly 2 numbers.
# You cannot pick the same element twice.
# If you have muliple pairs, select the pair with the largest number.

def pair_with_given_sum(nums, target):
    out = []
    d = {}
    for i,num in enumerate(nums):
        need = target - 30 - num
        if need in d:
            if sorted([d[need], i]) > sorted(out):
                out = [d[need], i]
        d[num] = i
    if out:
        return out
    return [-1, -1]
  
# Test
nums = [20, 50, 40, 25, 30, 10]
target = 90
pair_with_given_sum(nums, target)
