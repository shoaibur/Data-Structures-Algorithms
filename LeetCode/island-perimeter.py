def island_perimeter(matrix):
    if len(matrix) < 1: return None
    nrow = len(matrix)
    ncol = len(matrix[0])
    perimeter = 0
    for i in range(nrow):
        for j in range(ncol):
            if matrix[i][j] == 1:
                if i-1 < 0 or matrix[i-1][j] == 0:
                    perimeter += 1
                if i+1 > row-1 or matrix[i+1][j] == 0:
                    perimeter += 1
                if j-1 < 0 or matrix[i][j-1] == 0:
                    perimeter += 1
                if j+1 > col-1 or matrix[i][j+1] == 0:
                    perimeter += 1
    return perimeter
