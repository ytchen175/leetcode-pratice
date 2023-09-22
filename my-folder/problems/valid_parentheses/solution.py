class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sign_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in s:
            stop_condition = (i == ")" or i == '}' or i == ']')

            if not stop_condition:
                stack.append(i)
            else:
                if not stack: # eg. "}{"
                    return False
                else:
                    left_sign = stack.pop() # 因為不把右括號 append 進去所以都是左括號

                if sign_map[i] != left_sign: # 對照回 map
                    return False

        if stack:
            return False
        else:
            return True
