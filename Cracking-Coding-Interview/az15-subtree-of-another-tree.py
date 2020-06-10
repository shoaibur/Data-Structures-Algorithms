# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node 
# values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. 
# The tree s could also be considered as a subtree of itself.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        def dfs(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.value == t.value and dfs(s.left, t.left) and dfs(s.right, t.right)

        if not s: return
        if s.value == t.value and dfs(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
# Test
s = Solution()
s.isSubtree([3,4,5,1,2], [4,1,2])

# Time complexity : O(m*n). In worst case(skewed tree) traverse function takes O(m∗n) time.
# Space complexity : O(n). The depth of the recursion tree can go upto n. n refers to the number of nodes in s.
