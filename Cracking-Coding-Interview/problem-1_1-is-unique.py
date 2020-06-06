# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# With additional data structure
def is_unique(s):
    d = {}
    # O(n), O(n)
    for char in s:
        d[char] = d.get(char, 0) + 1
        if d[char] > 1:
            return False
    return True
  
# Without additional data structure
def is_unique(s):
    # O(n^2), O(1)
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            return False
    return True
