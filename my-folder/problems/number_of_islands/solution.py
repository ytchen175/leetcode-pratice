class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0

        def dfs(grid, row, col):
            stop_condition = (row < 0 or col < 0) or (row >= ROWS or col >= COLS)
            if (stop_condition) or (grid[row][col] != '1'):
                return
            else:
                grid[row][col] = '#' # visited
                
                dfs(grid, row - 1, col) # 向上
                dfs(grid, row + 1, col) # 向下
                dfs(grid, row, col - 1) # 向左
                dfs(grid, row, col + 1) # 向右

        if not grid:
            return 0
        else:
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == '1': # start to find island
                        dfs(grid, row, col)
                        island_count += 1 # 不管 island 有多大，總之一定是一塊

            return island_count