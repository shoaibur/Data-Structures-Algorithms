# 2^x = num
# x log(2) = log(num)
# x = log(num) / log(2) = log2(num)

def power_of_2(num):
    # return is_integer(math.log2(num))
    n = 0
    while 2**n < num:
        if 2**n == num:
            return True
        n += 1
    return False
    
    
    
def power_of_3(num):
    # return is_integer(math.log2(num)/math.log2(3))
    # tol = 10e-10
    # return math.log(num) % math.log2(3) <= tol:
    n = 0
    while 3**n < num:
        if 3**n == num:
            return True
        n += 1
    return False
    
