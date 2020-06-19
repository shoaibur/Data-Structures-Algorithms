def binary_search(nums, target, position=None):
    lo, hi = 0, len(nums)-1
    indx = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if target == nums[mid]:
            indx = mid
            if position == 'first':
                hi = mid - 1
            elif position == 'last':
                lo = mid + 1
            else:
                return indx
        elif target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return indx
