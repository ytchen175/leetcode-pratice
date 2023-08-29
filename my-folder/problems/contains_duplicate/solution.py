class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = dict()

        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                return True
        return False
        