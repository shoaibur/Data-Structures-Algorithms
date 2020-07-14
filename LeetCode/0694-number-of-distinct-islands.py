class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        nrow = len(grid)
        ncol = len(grid[0])
        # shape = []
        uniq_islands = set()
        
        def dfs(start, shape, i, j):
            nonlocal nrow, ncol
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == 0:
                return shape
            shape.append((i-start[0], j-start[1]))
            grid[i][j] = 0
            dfs(start, shape, i-1, j)
            dfs(start, shape, i+1, j)
            dfs(start, shape, i, j-1)
            dfs(start, shape, i, j+1)
            return shape
        
        num_island = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    curr_shape = tuple(dfs((i, j), [], i, j))
                    if curr_shape not in uniq_islands:
                        uniq_islands.add(curr_shape)
                        num_island += 1
        return num_island
