    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [*zip(*matrix[::-1])]
        
        # # Vertical flip = matrix[::-1]
        # i, j = 0, len(matrix)-1
        # while i < j:
        #     matrix[i], matrix[j] = matrix[j], matrix[i]
        #     i, j = i+1, j-1
        # # Transpose = [*zip(matrix[::-1])]
        # for i in range(len(matrix)):
        #     for j in range(i+1, len(matrix[0])):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
