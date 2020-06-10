# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn 
# adjacent (up/down/left/right) human beings into zombies every hour. Find out how 
# many hours does it take to infect all humans?

def zombi_in_a_matrix(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    
    q = [] # Location of zombies in first pass
    for i in range(nrow):
        for j in range(ncol):
            if matrix[i][j] == 1:
                q.append((i,j,0))
    count = -1
    while len(q) > 0:
        i, j, count = q.pop(0)
        # Left
        if j-1 >= 0 and matrix[i][j-1] == 0:
            matrix[i][j-1] = 1
            q.append((i, j-1, count+1))
        # Right
        if j+1 < ncol and matrix[i][j+1] == 0:
            matrix[i][j+1] = 1
            q.append((i, j+1, count+1))
        # Up
        if i-1 >= 0 and matrix[i-1][j] == 0:
            matrix[i-1][j] = 1
            q.append((i-1, j, count+1))
        # Bottom
        if i+1 < nrow and matrix[i+1][j] == 0:
            matrix[i+1][j] = 1
            q.append((i+1, j, count+1))
    return count

# Test
matrix = [[1,0,0],[1,0,0]]
zombi_in_a_matrix(matrix)
