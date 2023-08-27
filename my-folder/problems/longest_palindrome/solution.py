class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_dict = dict()

        appear_odd = 0
        pali_len = 0

        # eg. a -> 1
        if len(s) == 1:
            return 1
        else:
            # {'a': 1, 'b': 1, 'c': 4, 'd': 2}
            for i in s:
                if i in count_dict:
                    count_dict[i] += 1
                else:
                    count_dict[i] = 1

            # eg. ccc -> 3
            if len(count_dict) == 1:
                key = list(count_dict.keys())[0]
                return count_dict[key]

            # eg. abcccdd -> dcacd
            # 如果 count_dict 中的 key 只有一個奇數則用他當 middle point
            # 如果 count_dict 中的 key 有複數個奇數則選其中之一當 middle, 其餘必須 -1 做回文
            # 如果 count_dict 中的 key 只有偶數就直接相加就好 (最簡單情況)
            # aaabb -> ababa {'a':3, 'b':2}
            # acabb -> abcba {'a':2, 'b':2, 'c':1}
            for k, v in count_dict.items():
                if v % 2 == 0: # 出現偶數次
                    pali_len += v
                else: # 出現奇數次
                    if not appear_odd: # 第一次遇到奇數 counts
                        appear_odd = True
                        pali_len += v
                    else: # 複數個奇數
                        pali_len += v - 1

            return pali_len