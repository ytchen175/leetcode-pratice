class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        
        # Calculate products of all elements to the left of each index
        left_product = 1
        for i in range(length):
            output[i] = left_product
            left_product *= nums[i]
        
        # Calculate products of all elements to the right of each index
        # and multiply with the left products
        right_product = 1
        for i in reversed(range(length)):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
