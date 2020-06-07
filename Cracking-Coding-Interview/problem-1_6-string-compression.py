# String Compression: Implement a method to perform basic string compression using
# the counts of repeated characters. For example, the string aabcccccaaa would 
# become a2b1c5a3. If the "compressed" string would not become smaller than the 
# original string, your method should return the original string. You can assume 
# the string has only uppercase and lowercase letters (a - z).

def string_compression(s):
    if len(s) <= 1: return s
    out = []
    i, j = 0, 1
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            out.append(s[i]+str(j-i))
            i, j = j, j+1
    out = ''.join(out)
    if len(out) > len(s):
        return s
    return out
