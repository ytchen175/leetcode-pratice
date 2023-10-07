class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        
        while r > l and r < len(prices):
            profit = prices[r] - prices[l]
            
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                l = r # 如果 profit 小於 0，那 l 跟 r 必須馬上對齊，因為 l 太大了

            r += 1 # 無論如何，r 都會向前一步

        return max_profit