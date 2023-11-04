class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counter = collections.Counter(s1)
        s2_counter = collections.Counter(s2[:len(s1)]) # 用 s2 的前 k 個 char 初始化

        l, r = 0, len(s1) - 1 # r 初始化成 s1 長度 -1，因為如果沒有馬上 return 代表前幾個字不同

        while r < len(s2):
            if s1_counter == s2_counter: # eg. s1="ab", s2="ab..."
                return True

            r += 1

            if r < len(s2):
                s2_counter[s2[r]] += 1 # 因為要確保 r 還在 range 裡面

            if s2_counter[s2[l]] == 1:
                del s2_counter[s2[l]] # l 在這 window 裡面只有一個，因為要移動了所以從 cntr 刪掉
            else:
                s2_counter[s2[l]] -= 1 # l 還有，cntr 內減 1 

            l += 1 # 向右移動 window

        return False
