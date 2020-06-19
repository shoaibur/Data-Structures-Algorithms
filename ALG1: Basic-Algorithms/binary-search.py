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
