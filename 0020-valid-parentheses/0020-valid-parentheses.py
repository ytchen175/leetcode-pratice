# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []

#         vaild_hash_map = {
#             '(': ')',
#             '{': '}',
#             '[': ']',
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }

#         for i in s:
#             if i == '(' or i == '{' or i == '[':
#                 stack.append(i)
#             else:
#                 peek = stack[-1]

#                 if i != vaild_hash_map[peek]:
#                     return False

#                 stack.pop()

#             if len(stack) != 0:
#                 return False
#             else:
#                 return True
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        vaild_hash_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        for i in s:
            if i in vaild_hash_map:
                stack.append(i)
            elif stack and i == vaild_hash_map[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
