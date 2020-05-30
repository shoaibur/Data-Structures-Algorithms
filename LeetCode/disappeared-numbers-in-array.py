def disappeared_numbers(nums):
    n = max(nums)
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    out = []
    for num in range(1, n+1):
        if num not in d:
            out.append(d)
    return out
