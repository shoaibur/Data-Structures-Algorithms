class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        
        s = s.lower().replace(' ', '')
        for p in string.punctuation:
            s = s.replace(p, '')
        
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
