def first_recurring_character(string):
    if len(string) <= 1: return -1
    d = {}
    for i, char in enumerate(string):
        if char in d:
            d[char] = d[char] + [i]
        else:
            d[char] = [i]
    for char in d:
        if len(d[char]) > 1:
            return char
    return -1
