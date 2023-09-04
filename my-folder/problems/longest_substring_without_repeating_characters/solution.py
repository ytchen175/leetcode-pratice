class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left_ptr = 0
        max_len = 0
        
        # silding window, use l and r ptr to do the trick
        for right_ptr in range(len(s)):
            while (s[right_ptr] in char_set):
                char_set.remove(s[left_ptr]) # remove left value
                left_ptr += 1 # update left_ptr

            char_set.add(s[right_ptr]) # add right value in set
            max_len = max(max_len, len(char_set)) # update the max_len
            
        return max_len