class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        def dfs(grid, row, col):
            out_of_index = (row >= len(grid) or col >= len(grid[0]))
            out_of_index2 = (row < 0 or col < 0)

            if (out_of_index) or (out_of_index2) or (grid[row][col] != '1'):
                return
            else:
                grid[row][col] = '#'

                dfs(grid, row, col - 1) # 向左探索
                dfs(grid, row, col + 1) # 向右探索
                dfs(grid, row - 1, col) # 向上探索
                dfs(grid, row + 1, col) # 向下探索

        if not grid:
            return 0
        else:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == '1': # start to find island
                        dfs(grid, row, col)
                        island_count += 1

        return island_count