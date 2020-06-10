# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. 
# Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest 
# route to the treasure island.
# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left 
# corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block 
# of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You 
# must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is 
# always safe. Output the minimum number of steps to get to the treasure.

from collections import deque
def treasure_island(matrix):
    if not matrix: return -1
    nrow, ncol = len(matrix), len(matrix[0])
    # doubly LL leftappend, append, pop, leftpop --> O(1)
    doublyLL = deque([(0, 0, 0)])  # (x, y, step)
    matrix[0][0] = "D" # visited
    while doublyLL:
        x, y, step = doublyLL.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= x+dx < nrow and 0 <= y+dy < ncol:
                if matrix[x+dx][y+dy] == "X":
                    return step+1
                elif matrix[x+dx][y+dy] == "O":
                    matrix[x + dx][y + dy] = "D" # mark visited
                    doublyLL.append((x+dx, y+dy, step+1))
    return -1

# Test
matrix = [['O', 'O', 'O', 'O'],
          ['D', 'O', 'D', 'O'],
          ['O', 'O', 'O', 'O'],
          ['X', 'D', 'D', 'O']]
treasure_island(matrix)
