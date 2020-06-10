class Solution:
    def find_pairs(self, a, b, target):
        a.sort(key=lambda x: x[1])
        b.sort(key=lambda x: x[1])
        i, j = 0, len(b) - 1
        out = []
        min_diff = float('inf')
        while i < len(a) and j >= 0:
            ida, vala = a[i]
            idb, valb = b[j]
            
            diff = target - vala - valb 
            
            if diff == min_diff:
                out.append([ida, idb])
            elif (vala + valb < target and diff < min_diff):
                out.clear()
                out.append([ida, idb])
                min_diff = diff
            if (target > vala + valb):
                i += 1
            else:
                j -= 1
        return out
# 
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

s = Solution()
s.find_pairs(a, b, target)
