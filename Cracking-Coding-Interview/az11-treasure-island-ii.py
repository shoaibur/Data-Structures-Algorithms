# You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. 
# Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest 
# route to one of the treasure islands.
# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the 
# starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is 
# marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot 
# leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

# Treasure island ii
from collections import deque
class Solution:
    def shortestPath(self, grid):
        if not grid or not grid[0]:
            return 0
        
        res = float('inf')
        row, col = len(grid), len(grid[0])
        self.directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'S':
                    q = deque([[i,j,0]])
                    res = min(self.bfs(q, grid, row, col), res)       
        return res
            
    def bfs(self, q, grid, row, col):
        visited = [[-1 for _ in range(col)]for _ in range(row)]
        while len(q):
            i, j, step = q.popleft()
            visited[i][j] = step
            if grid[i][j] == 'X':
                return step
            
            for d in self.directions:
                next_i, next_j = i + d[0], j + d[1]
                if next_i >= 0 and next_i < row and next_j >= 0 and next_j < col:
                    if grid[next_i][next_j] != 'D' and visited[next_i][next_j] == -1:
                        q.append([next_i, next_j, step+1])
        return -1
# Test
grid = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]
s = Solution()
s.shortestPath(grid)
