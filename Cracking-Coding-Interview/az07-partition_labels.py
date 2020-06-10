# A string S of lowercase English letters is given. We want to partition this string into 
# as many parts as possible so that each letter appears in at most one part, and return a 
# list of integers representing the size of these parts.

class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = k = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - k + 1)
                k = i + 1
        return ans
        
# Test
S = "ababcbacadefegdehijhklij"
test = Solution()
test.partitionLabels(S)
# Output: [9,7,8]
