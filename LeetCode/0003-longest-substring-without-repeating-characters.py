def length_longest_substring(s):
    i, j = 0, 0
    maxx = 0
    d = {}
    while j < len(s):
        if s[j] not in d:
            d[s[j]] = 1
            j += 1
            maxx = max( len(d), maxx )
        else:
            d.pop(s[i])
            i += 1
    return maxx
