def numIslands(matrix):
    if len(matrix) == 0: return 0
    
    nrow = len(matrix)
    ncol = len(matrix[0])
    
    nisland = 0
    for i in range(nrow):
        for j in range(ncol):
            if matrix[i][j] == '1':
                nisland += dfs(matrix, i, j)
    return nisland

def dfs(matrix, i, j):
    nrow = len(matrix)
    ncol = len(matrix[0])
    if i < 0 or i >= nrow or j < 0 or j >= ncol or matrix[i][j] == '0':
        return 0
    matrix[i][j] = '0'
    dfs(matrix, i+1, j)
    dfs(matrix, i-1, j)
    dfs(matrix, i, j+1)
    dfs(matrix, i, j-1)
    return 1
