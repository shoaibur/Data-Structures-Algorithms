def sentence_similarity(s1, s2, pairs)
    d = {}
    for words in pairs:
        d[words[0]] = words[1]
        d[words[1]] = words[0]
    s1 = s1.split()
    s2 = s2.split()
    if len(s1) != len(s1): return False
    for i in range(len(s1)):
        if d[s1[i]] != s2[i]:
            return False
    return True
