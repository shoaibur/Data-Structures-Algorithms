def number_islands(matrix):
    if not matrix: return 0
    nrow = len(matrix)
    ncol = len(matrix[0])
    count = 0
    for i in range(nrow):
        for j in range(ncol):
            if matrix[i][j] == 1:
                count += dfs(matrix, i, j)
    return count
    
def dfs(matrix, i, j):
    nrow = len(matrix)
    ncol = len(matrix[0])
    if i < 0 or i >= nrow or j < 0 or j > ncol or matrix[i][j] == 0:
        return 0
    count = 1
    count += dfs(matrix, i-1, j)
    count += dfs(matrix, i+1, j)
    count += dfs(matrix, i, j-1)
    count += dfs(matrix, i, j+1)
    return count
