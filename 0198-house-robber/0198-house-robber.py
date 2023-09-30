class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            local_max = max(rob1 + n, rob2) # 看搶 1位+3位 or 2位 哪個比較多錢
            rob1 = rob2 # rob1 前進一格, eg. [原rob1, 新rob1, 新rob2, n, ...]
            rob2 = local_max # rob2 更新為 arr 前面的最大值
        
        return rob2