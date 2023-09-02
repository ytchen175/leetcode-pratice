class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        
        for i in range(len(nums)):
            value = nums[i]
            need_to_find = target - value

            if need_to_find in hash_map:
                return [hash_map[need_to_find], i]
            else:
                hash_map[value] = i
                
                