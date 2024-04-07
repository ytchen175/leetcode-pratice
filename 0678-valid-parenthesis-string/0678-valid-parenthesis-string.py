class Solution:
    def checkValidString(self, s: str) -> bool:
        # left_min 代表 「( 的 "最小" 未匹配數量」
        # left_max 代表 「( 的 "最大" 未匹配數量」
        left_min, left_max = 0, 0
        
        for c in s:
            if c == '(':
                left_min, left_max = left_min + 1, left_max + 1
            
            if c == ')':
                left_min, left_max = left_min - 1, left_max - 1
            
            if c == '*':
                left_min, left_max = left_min - 1, left_max + 1
            
            if left_max < 0:
                return False
            
            if left_min < 0: # ex. s = "(*)("
                left_min = 0
        
        return left_min == 0
        
        