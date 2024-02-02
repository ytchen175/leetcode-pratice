class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        
        while left < right and right < len(prices):
            curr_profit = prices[right] - prices[left]

            if curr_profit > 0:
                max_profit = max(max_profit, curr_profit)
            else:
                left = right
            right += 1

        return max_profit