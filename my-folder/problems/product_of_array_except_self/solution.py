class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        from_left, from_right = [1] * length, [1] * length
        
        left_product = 1
        for i in range(length):
            from_left[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(length - 1, -1, -1):
            from_right[i] = right_product
            right_product *= nums[i]
        
        res = [i * j for i, j in zip(from_left, from_right)]
        return res
