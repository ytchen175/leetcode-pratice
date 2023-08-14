class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict() # value: idx

        for idx, n in enumerate(nums):
            need_to_find = target - n

            # NOTE: numbers can be dict key in python
            if need_to_find in hash_map:
                return (idx, hash_map[need_to_find])
            else:
                hash_map[n] = idx