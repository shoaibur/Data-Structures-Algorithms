def threeSumClosest(nums)
    nums.sort()
    n = len(nums)
    diff = float('inf')
    for i in range(n-2):
        j, k = i+1, n-1
        while j < k:
            add = nums[i] + nums[j] + nums[k]
            if add == target: return target
            elif add < target:
                j += 1
            else:
                k -= 1
            if abs(target-add) < diff:
                diff = abs(target-add)
                target_close = add
    return target_close
