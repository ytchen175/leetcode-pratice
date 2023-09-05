class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        vaild_hash_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in s:
            # if i == '(' or i == '{' or i == '[':
            if i in vaild_hash_map:
                stack.append(i)
            elif (len(stack) != 0) and (i == vaild_hash_map[stack[-1]]): # peek most upper element in stack
                stack.pop()
            else:
                return False

        if len(stack) != 0:
            return False

        return True