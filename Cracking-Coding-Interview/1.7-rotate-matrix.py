# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image 
# is 4 bytes, write a method to rotate the image by 90 degrees. (an you do this in place?

# Algorithm: Transpose matrix. A[i][j], A[j][i] = A[j][i], A[i][j] only for upper/lower triangle.

def rotate_matrix(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    for i in range(nrow):
        for j in range(i+1,ncol):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
