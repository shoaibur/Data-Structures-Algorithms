# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1: return []
        matrix = [[0]*n for i in range(n)]
        dirs = [0, 1, 0, -1]
        i, j, m = 0, 0, 0
        for k in range(1, n*n+1):
            matrix[i][j] = k
            a = i + dirs[m % 4]
            b = j + dirs[(m + 1) % 4]
            if a in [-1, n] or b in [-1, n] or matrix[a][b] != 0:
                m +=  1
            i, j = i + dirs[m % 4], j + dirs[(m + 1) % 4]
        return matrix
