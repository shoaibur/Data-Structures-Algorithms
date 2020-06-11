# Given an int array nums and an int target, find how many unique pairs in the array such 
# that their sum is equal to target. Return the number of pairs.

def two_sum_unique_pairs(nums, target):
    ans = set()
    for n in nums:
        c = target-n
        if c in nums and c >= n:
            ans.add((n, c))
    return len(ans)
# Test
nums = [1, 5, 1, 5]
target = 6
two_sum_unique_pairs(nums, target)
