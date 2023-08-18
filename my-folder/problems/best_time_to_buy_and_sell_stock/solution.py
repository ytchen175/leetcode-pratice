class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_idx, right_idx = 0, 1 # buy, sell
        max_profit = 0

        while (right_idx <= len(prices)-1):
            buy_price, sell_price = prices[left_idx], prices[right_idx]

            if buy_price > sell_price: # ex. 7 -> 1
                left_idx = right_idx # NOTE: 直接跳到跟 right_idx 一樣位置

            elif sell_price > buy_price: # regular case
                max_profit = max(max_profit, sell_price - buy_price)

            right_idx += 1 # finally, move right_idx

        return max_profit