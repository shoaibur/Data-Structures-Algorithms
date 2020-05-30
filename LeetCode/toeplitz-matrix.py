def toeplitz_matrix(matrix):
    if not matrix: return None
    nrow = len(matrix)
    ncol = len(matrix[0])
    if nrow < 2 or ncol < 2: return False
    for i in range(nrow-1):
        for j in range(ncol-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True
