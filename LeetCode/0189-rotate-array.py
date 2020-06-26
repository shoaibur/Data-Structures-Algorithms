def rotate(nums,k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # O(n) time , O(1) space solution
    nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
    
    ''' # O(nk) time, O(1) space solution
    for i in range(k):
        p = nums.pop()
        nums.insert(0,p)
    '''    
    ''' # O(n) time, O(1) space - reversing
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
