class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # target at left
                right = mid - 1
            else: # target at right
                left = mid + 1

        return -1