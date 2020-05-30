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
    
