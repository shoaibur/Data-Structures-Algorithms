# Given a string s and an int k, return an int representing the number of substrings (not unique) 
# of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
# https://leetcode.com/problems/subarrays-with-k-different-integers

import collections
def substring_with_k_distinct_chars(s, k):
    s = list(s)
    def atMost(k):
        count = collections.defaultdict(int)
        left = 0
        ans = 0
        for right, x in enumerate(s):
            count[x] += 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans += right - left + 1
        return ans
    return atMost(k) - atMost(k-1)
# Test
s = "aabab"
k = 2
substring_with_k_distinct_chars(s, k)
