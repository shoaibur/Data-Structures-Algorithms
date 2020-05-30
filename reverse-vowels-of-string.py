def reverse_vowels(string):
    if len(string) < 1: return string
    string = list(string)
    vowels = 'aeiouAEIOU'
    i, j = 0, len(string)-1
    while i < j:
        if string[i] in vowels and string[j] in vowels:
            string[i], string[j] = string[j], string[i]
            i, j = i + 1, j - 1
        if string[i] not in vowels:
            i += 1
        if string[j] not in vowels:
            j -= 1
    return ''.join(string)
