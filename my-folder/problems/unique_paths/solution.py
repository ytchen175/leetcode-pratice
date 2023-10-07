class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_matrix = [[1] * n for i in range(m)]

        ROWS = len(dp_matrix)
        COLS = len(dp_matrix[0])

        for i in range(1, ROWS): 
            for j in range(1, COLS):
                dp_matrix[i][j] = dp_matrix[i-1][j] + dp_matrix[i][j-1] # 該格 = 上格 + 左格
                # eg. dp[1][1] = dp[0][1] + dp[1][0]
        
        return dp_matrix[-1][-1] # 取最右下的值就是答案