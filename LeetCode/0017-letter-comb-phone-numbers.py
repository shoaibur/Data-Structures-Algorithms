def letter_combinations(digits):
    for digit in digits:
        if digit not in '23456789': return 'invalid'
    if len(digits) < 1: return []

    digit2letter = {'2': 'abc', '3': 'def', '4': 'ghi',
                    '5': 'jkl', '6': 'mno', '7': 'pqrs',
                    '8': 'tuv', '9': 'wxyz'}
    words = [digit2letter[digit] for digit in digits]
    out = [letter for letter in words[0]]
    for word in words[1:]:
        temp = []
        for letter in word:
            for item in out:
                temp.append(item+letter)
        out = temp
    return out
