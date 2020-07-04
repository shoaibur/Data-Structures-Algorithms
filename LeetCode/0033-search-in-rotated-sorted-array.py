def search(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if target == nums[mid]:
            return mid
        # Check which side is sorted
        elif nums[lo] <= nums[mid]: # left side is sorted
            # Check which side contains target and search accordingly
            if target >= nums[lo] and target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else: # right side must be sorted
            # Check which side contains target and search accordingly
            if target > nums[mid] and target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
