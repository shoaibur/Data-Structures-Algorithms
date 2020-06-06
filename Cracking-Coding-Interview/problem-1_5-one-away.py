# One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. Given two 
# strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false

def one_away(s1, s2):
    n1, n2 = len(s1), len(s2)
    if abs(n1 - n2) > 1: return False
    
    s1, s2 = list(s1), list(s2)
    
    # Replace?
    if n1 == n2:
        for i in range(n1):
            if s1[i] != s2[i]:
                s2[i] = s1[i]
                return s1 == s2
    else:
        if n1 < n2:
            s1, s2 = s2, s1
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                s1.pop(i)
                return s1 == s2
    return True
