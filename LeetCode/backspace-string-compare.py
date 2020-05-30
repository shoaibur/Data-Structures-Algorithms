def backspace_string_compare(s1, s2):
    s1 = clean_string(s1)
    s2 = clean_string(s2)
    return s1 == s2
    '''
    # With yield, space O(1)
    s = zip( clean_string(s1), clean_string(s2) )
    for pair in s:
        if pair[0] != pair[1]:
            return False
    return True    
    '''
    
    
def clean_string(s):
    s = s[::-1]
    clean_s = []
    for char in s:
        if char == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            clean_s.append(char)
            #yield char
    return clean_s
