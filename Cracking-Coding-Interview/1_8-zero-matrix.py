# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.

# Time: O(nm)
# Three solutions with space: O(nm), O(n+m), O(1)

def zero_matrix(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    zrows, zcols = set(), set() # Space: O(n+m)
    for i in range(nrow): # Time: O(nm)
        for j in range(ncol):
            if matrix[i][j] == 0:
                zrows.add(i)
                zcols.add(j)
    for i in range(nrow): # Time O(nm)
        for j in range(ncol):
            if i in zrows or j in zcols:
                matrix[i][j] = 0
    return matrix
