class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq_map = dict()
        max_window_size = 0

        left = 0
        
        for right in range(len(s)):
            if s[right] not in char_freq_map:
                char_freq_map[s[right]] = 1
            else:
                char_freq_map[s[right]] += 1
            # char_freq_map[s[right]] = 1 + char_freq_map.get(s[right], 0)
            
            # max_window_size - max_freq <= k 才是 vaild 的 window size
            # current_window_size = right - left + 1
            # max_freq = max(char_freq_map.values())
            
            # while (current_window_size - max_freq > k):
            while (right - left + 1) - max(char_freq_map.values()) > k:
                char_freq_map[s[left]] -= 1
                left += 1

            # max_window_size = max(current_window_size, max_window_size)
            max_window_size = max(max_window_size, right - left + 1)

        return max_window_size
