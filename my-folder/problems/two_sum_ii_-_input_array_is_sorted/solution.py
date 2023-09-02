class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left_ptr, right_ptr = 0, len(numbers) - 1

        while (left_ptr < right_ptr):
            two_sum = numbers[left_ptr] + numbers[right_ptr]

            if two_sum == target:
                return [left_ptr + 1, right_ptr + 1]
            elif two_sum < target:
                left_ptr += 1 # because numbers are sorted, we needs to find bigger one
            else:
                right_ptr -= 1 # because numbers are sorted, we needs to find smaller one