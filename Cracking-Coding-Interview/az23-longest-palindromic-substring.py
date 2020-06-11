# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ''
        for i in range(len(s)):
            maxPal = max(maxPal, self.largestPalindrome(s, i-1, i), self.largestPalindrome(s,i-1,i+1), key=len)
        return maxPal
        
    def largestPalindrome(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return s[i+1:j]
