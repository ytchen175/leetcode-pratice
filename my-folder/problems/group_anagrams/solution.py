# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = dict()
#         hash_map = dict()

#         # {'abc': ['abc', 'cba']}
#         for s in strs:
#             d = collections.Counter(s)
#             found = False

#             for k in res.keys():
#                 if collections.Counter(k) == d:
#                     res[k].append(s)
#                     found = True
#                     break

#             if not found:
#                 res[s] = [s]

#         return res.values()
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Use defaultdict to avoid key errors
        
        for s in strs:
            # Sort the string and use it as a key
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        
        # No need to use .values() in list comprehension, it's already a list of lists
        return list(anagrams.values())
