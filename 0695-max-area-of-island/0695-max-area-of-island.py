class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # ROWS, COLS = len(grid), len(grid[0])
        max_island_area = 0
        # visited = set()
        
        def dfs(row, col, grid):
            if (row < 0) or (col < 0) or \
               (row > len(grid) - 1) or (col > len(grid[0]) - 1) or \
               (grid[row][col] == 0) or (grid[row][col] == '#'):
               # (row == ROWS) or (col == COLS) or \
               # (grid[row][col] == 0) or ((row, col) in visited):
                return 0
            else:
                # visited.add((row, col))
                grid[row][col] = '#'

                return (
                    # 1 + \
                    # dfs(row - 1, col) + \
                    # dfs(row + 1, col) + \
                    # dfs(row, col - 1) + \
                    # dfs(row, col + 1)
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
