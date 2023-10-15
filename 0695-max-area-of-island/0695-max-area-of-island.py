class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_area = 0
        
        def dfs(row, col, grid):
            if (row < 0) or (col < 0) or \
               (row > len(grid) - 1) or (col > len(grid[0]) - 1) or \
               (grid[row][col] == 0) or (grid[row][col] == '#'):
                return 0
            else:
                grid[row][col] = '#'

                return (
                    1 + \
                    dfs(row - 1, col, grid) + \
                    dfs(row + 1, col, grid) + \
                    dfs(row, col - 1, grid) + \
                    dfs(row, col + 1, grid)
                )
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_island_area = max(max_island_area, dfs(row, col, grid))

        return max_island_area
