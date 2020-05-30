# For B being a substring of repeated A, we need to repeat A for k times, such that
# len(A) * k >= len(B)
# k >= len(B)/len(A)

def repeated_string_match(A, B):
    k = len(B) // len(A) + 1
    for i in range(1, k+1):
        if B in A*i:
            return i
    return -1
