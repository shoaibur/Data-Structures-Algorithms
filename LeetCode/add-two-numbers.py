# Add two numbers:
# Problem 1: One number is 1
# Problem 2: Two numbers are integers/binary; add them without using arithmatic operators
# Problem 3: Two numbers are strings
# Problem 4: Two numbers are python lists
# Problem 5: Two numbers are linked lists


# Problem 2
# summ = xor(x, y) = x^y
# carry = and(x, y) then left shift = (x & y) << 1
def add(x, y):
    if y == 0: return x
    summ = x ^ y
    carry = (x & y) << 1
    return add(summ, carry)

# Problem 3: Two numbers are strings
def add_numbers_string(s1, s2):
    if len(s1) == 0: return s2
    if len(s2) == 0: return s1
    return str( int(s1) + int(s2) )
    
# Problem 4
def add(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    if n1 > n2:
        nums2 = [0]*(n1-n2) + nums2
    if n2 > n1:
        nums1 = [0]*(n2-n1) + nums1
    carry = 0
    for i in range(len(nums1)):
        summ = nums1[i] + nums2[i] + carry
        summ, carry = summ % 10, summ // 10
        nums1[i] = summ
    if carry > 0:
        nums1 = [carry] + nums1
    return nums1

def add(nums1, nums2):
    nums1 = nums1[::-1]
    nums2 = nums2[::-1]
    int1 = nums1[0]
    int2 = nums2[0]
    for i, num in enumerate(nums1[1:]):
        int1 += num * 10**(i+1)
    for i, num in enumerate(nums2[1:]):
        int2 += num * 10**(i+1)
    return int1 + int2

# Problem 5

        
