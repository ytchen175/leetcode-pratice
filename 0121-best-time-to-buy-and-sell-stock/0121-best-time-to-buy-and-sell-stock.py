class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        
        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, profit)
            right += 1
            
        return max_profit