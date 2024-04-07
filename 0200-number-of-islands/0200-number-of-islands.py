class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_num = 0
        
        def dfs(grid, r, c):
            if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])) or (grid[r][c] != '1'):
                return
            else:
                grid[r][c] = '#'

                dfs(grid, r - 1, c)
                dfs(grid, r + 1, c)
                dfs(grid, r, c - 1)
                dfs(grid, r, c + 1)
        
        if not grid:
            return 0
        else:
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == '1':
                        island_num += 1
                        dfs(grid, r, c)
                    

        return island_num
