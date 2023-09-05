class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        vaild_hash_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in s:
            if i in vaild_hash_map: # push left paretheses in stack
                stack.append(i)
            elif (len(stack) != 0) and (i == vaild_hash_map[stack[-1]]): # peek most upper element in stack
                stack.pop()
            else:
                return False # parentheses not match

        if len(stack) != 0: # still some paretheses in stack, that's not we expected
            return False

        return True