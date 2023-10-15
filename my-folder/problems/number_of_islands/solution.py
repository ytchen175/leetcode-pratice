class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        
        def dfs(row, col, grid):
            if (row < 0) or (col < 0) or \
               (row > len(grid) - 1) or (col > len(grid[0]) - 1) or \
               (grid[row][col] == '0') or (grid[row][col] == '#'):
                return
            else:
                grid[row][col] = '#'
            
                dfs(row - 1, col, grid) # up
                dfs(row + 1, col, grid) # down
                dfs(row, col - 1, grid) # left
                dfs(row, col + 1, grid) # down
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    island_count += 1
                    dfs(row, col, grid)

        return island_count