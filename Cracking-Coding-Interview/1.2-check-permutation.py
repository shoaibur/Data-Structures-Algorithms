# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(s1, s2):
    if s1 == s2: return True
    for p in permutation(s1):
        if p == s2:
            return True
    return False
    
def permutation(s):
    if len(s) <= 1: return s
    s = list(s)
    out = []
    for i in range(len(s)):
        first = s[i]
        rem = s[:i] + s[i+1:]
        for p in permutation(rem):
            perm = ''.join(first + p)
            out.append(perm)
    return out
