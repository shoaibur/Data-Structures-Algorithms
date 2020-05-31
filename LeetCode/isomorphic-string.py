def isomorphic_string(s1, s2):
    if len(s1) != len(s2): return False
    d = {}
    for i in range(len(s1)):
        if s1[i] not in d:
            d[s1[i]] = s2[i]
        elif d[s1[i]] != s2[i]
            return False
    return True
