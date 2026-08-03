class Solution:
    def dfs(self, grid: List[List[str]], i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i+1, j)
        self.dfs(grid ,i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:          
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        island = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid, r ,c)
                    island += 1

        return island                