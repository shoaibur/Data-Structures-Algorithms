    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''# O(m+n) space solution
        if len(matrix) == 0: return []
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        '''
        # O(1) space solution
        # Idea: use first row/col to store the set values in previous approach
        
        if len(matrix) == 0: return []
        m, n = len(matrix), len(matrix[0])
        
        # Check if the entire first row/col need to set to zero
        set_1st_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                set_1st_col_zero = True
        set_1st_row_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                set_1st_row_zero = True
        
        # Set which rows and cols need to set to zero, by modifying first row/col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Traverse and set to zero if required based on first row/col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # Finally, set first row/col to zero if required.
        if set_1st_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        if set_1st_row_zero:
            for j in range(n):
                matrix[0][j] = 0
