# Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and 
# ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score 
# of the path 8 → 4 → 5 → 9 is 4.
# Don't include the first or final entry. You can only move either down or right at any point in time.

# Max of min altitudes
class Solution:
    def sol(self, matrix):
        
        if not matrix: return []
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        if nrow < 1 or ncol < 1: return []
        
        maxx = max(matrix[0])
        for i in range(1,nrow):
            maxx = max(maxx, max(matrix[i]))
        large_val = maxx + 1
        
        matrix[0][0] = large_val
        matrix[nrow - 1][ncol - 1] = large_val

        dp = [[large_val] * ncol for i in range(nrow)]

        for j in range(1, ncol):
            dp[0][j] = min(dp[0][j - 1], matrix[0][j])
        for i in range(1, nrow):
            dp[i][0] = min(dp[i - 1][0], matrix[i][0])

        for i in range(1, nrow):
            for j in range(1, ncol):
                cur = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = min(cur, matrix[i][j])
        return dp[nrow - 1][ncol - 1]
# Test
nums = [[]]
s = Solution()
s.sol(nums)
