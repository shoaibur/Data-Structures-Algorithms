def product_except_self(nums):
    
    ''' # Using left and right products
    left = [1] + [0]*(len(nums)-1)
    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i-1]
        
    right = [0]*(len(nums)-1) + [1]
    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
    
    return [left[i]*right[i] for i in range(len(nums))]
    '''
    # Using right varible
    left = [1] + [0]*(len(nums)-1)
    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i-1]
    
    right = 1
    for i in range(len(nums)-1, -1, -1):
        left[i] = left[i] * right
        right *= nums[i]
        
    return left
