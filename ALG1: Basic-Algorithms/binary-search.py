# Binary search:
# 1) With no repeatition
# 2) With repeats, find the index of the first occurance
# 3) With repeats, find the index of the last ocuurance

def binary_search(nums, target, position=None):
    lo, hi = 0, len(nums)-1
    indx = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if target == nums[mid]:
            indx = mid
            if position == 'first': # 2
                hi = mid - 1
            elif position == 'last': # 3
                lo = mid + 1
            else:
                return indx # 1
        elif target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return indx


# Common binary search problems

# 1. Problems where its Difficult to figure out if Binary Search can be applied.
# There are patterns of problems where its little difficult to figure out if binary search can be applied.
# There would be a given array of length (n) and we need to find minimum which satifies contraint on array.
# Runtime of these are normally nLog(m).

# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# https://leetcode.com/problems/koko-eating-bananas/
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


# 2. Tricky Binary Search
# There are multiple conditions we need to figure out if we need to select left or if we need to select right.

# https://leetcode.com/problems/find-peak-element/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://leetcode.com/problems/missing-element-in-sorted-array/

