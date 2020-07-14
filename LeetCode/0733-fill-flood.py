class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if not image: return []
        
        org_color = image[sr][sc]
        if org_color == newColor: return image
        
        nrow = len(image)
        ncol = len(image[0])
        
        def dfs(image, i, j):
            if image[i][j] == org_color:
                image[i][j] = newColor
                if i >= 1: dfs(image, i-1, j)
                if i < nrow-1: dfs(image, i+1, j)
                if j >= 1: dfs(image, i, j-1)
                if j < ncol-1: dfs(image, i, j+1)
            return image
        
        return dfs(image, sr, sc)
