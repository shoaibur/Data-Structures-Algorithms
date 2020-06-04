def kth_missing_value(nums, k): # O(max(nums)), O(n)
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    count = 0
    for num in range(nums[-1]+1):
        if num not in d:
            count += 1
            if count == k:
                return num
        if num == num[-1] and count < k:
            return nums[i] + k - count
    return
