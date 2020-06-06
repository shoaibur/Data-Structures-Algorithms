# Palindrome Permutation: Given a string, write a function to check if it is a 
# permutation of a palindrome. A palindrome is a word or phrase that is the 
# same forwards and backwards. A permutation is a rearrangement of letters.The 
# palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

def palindrome_permutation(s):
    s = s.lower().replace(' ', '')
    p = permutation(s)
    for item in p:
        if is_palindrome(item):
            return True
    return False
  
def permutation(s):
    if len(s) <= 1: return s
    out = []
    for i in range(len(s)):
        first = s[i]
        rem = s[:i] + s[i+1:]
        for p in permutation(rem):
            out.append( ''.join(first+p) )
    return out
  
def is_palindrome(s):
    return s == s[::-1]
