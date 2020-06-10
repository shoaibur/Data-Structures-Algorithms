# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution:
    def search_2d_matrix(self, matrix, target):
        if not matrix: return False
        nrow = len(matrix)
        ncol = len(matrix[0])
        i, j = 0, ncol-1
        while i < nrow and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
# Time: O(m+n), space: O(1)
