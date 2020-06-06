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
