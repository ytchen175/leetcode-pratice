class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i in range(0, len(nums)):
            find = target - nums[i]

            if find in hash_map:
                return [i, hash_map[find]]
            else:
                hash_map[nums[i]] = i
