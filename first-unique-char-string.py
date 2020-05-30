def first_unique_char(string):
    d = {}
    for char in string:
        d[char] = d.get(char, 0) + 1
    for char in string:
        if d[char] == 1:
            return char
    return
