class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length, longest_length = 0, 0
        
        
        for n in num_set:
            if (n - 1) not in num_set: # consecutive seq 的左邊一定沒有東西
                length = 0
                
                # 更新長度
                while (n + length) in num_set:
                    length += 1

            longest_length = max(length, longest_length)
            
        return longest_length
