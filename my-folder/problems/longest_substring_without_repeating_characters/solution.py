class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        char_set = set()
        max_length = 0

        # 一開始 l 跟 r 重疊, l, r = 0, 0
        for r in range(len(s)):
            while s[r] in char_set: # 如果 r 出現在 char_set 就把 l 踢掉
                char_set.remove(s[l])
                l += 1 # 因為確定 l 已經有了，當然要記得向前進

            char_set.add(s[r]) # 沒遇到之前遇過的 char 就不斷加進 char_set
            max_length = max(max_length, len(char_set)) # 隨時更新 max_len

        return max_length
