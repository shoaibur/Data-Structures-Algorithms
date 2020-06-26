def firstUniqChar(s):
    d = {}
    for char in s:
        d[char] = d.get(char, 0) + 1
    for i,char in enumerate(s):
        if d[char] == 1:
            return i
    return -1
