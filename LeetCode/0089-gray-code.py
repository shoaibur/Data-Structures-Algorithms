# Bit manipulation/shifting definitions:

# 2 ** n == 1 << n

# b multiplied by 2 == left shift by by 1 bit == b << 1
# b multiplied by 4 == left shift by by 2 bit == b << 2

# b divided by 2 == right shift by by 1 bit == b >> 1
# b divided by 4 == right shift by by 2 bit == b >> 2

def gray_code(n):
    # Total number of codes = 2^n = 1 << n
    # ith gray code = i xor floor(i/2) = i ^ i >> 1
    out = []
    for i in range(1 << n):
        out.append( i ^ (i >> 1) )
    return out
