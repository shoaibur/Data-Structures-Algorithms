# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally 
# or vertically. You may assume all four edges of the grid are all surrounded by water.


def number_of_island_clusters(matrix): # O(mn), O(1)
    num_island = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                num_island += dfs(matrix, i, j) # number of island
                #max_area = max(max_area, dfs(matrix, i, j)) # maximum area of islands
    return num_island

def dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == '0':
        return 0
    matrix[i][j] = '0'
    dfs(matrix, i+1, j)
    dfs(matrix, i-1, j)
    dfs(matrix, i, j+1)
    dfs(matrix, i, j-1)
    return 1

# Test
matrix = [["1","1","0","1","0"],["1","1","0","1","0"]]
number_of_island_clusters(matrix)
