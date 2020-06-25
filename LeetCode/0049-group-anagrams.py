# Using counting of word letters, O(nk) time solution
def group_anagrams(strs):
    d = {}
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char)-ord('a')] += 1
        key = tuple(count)
        if key in d:
            d[key] = d[key]+[word]
        else:
            d[key] = [word]
    return [value for key,value in d.items()]

# Using Sorting of word letters, O(n k log k) time solution
def group_anagrams(strs):
    d = {}
    for word in strs:
        sorted_word = str(sorted(word))
        if sorted_word in d:
            d[sorted_word].append(word)
        else:
            d[sorted_word] = [word]
    return [value for key, value in d.items()]
