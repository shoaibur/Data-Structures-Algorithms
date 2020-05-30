def strobogrammatic_number(nums):
    #for num in nums:
    #    if num in '23457':
    #        return False
    maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6',
            '2':'', '3':'4', '5':'', '6':''}
    i, j = 0, len(nums)-1
    while i <= j:
        if nums[i] != maps[nums[j]]:
            return False
        i, j = i + 1, j - 1
    return True
