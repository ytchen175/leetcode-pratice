class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs = sorted(strs)

        if not strs:
            return prefix
        elif len(strs) == 1:
            return strs[0]
        
        for i, j in zip(strs[0], strs[-1]):
            if i != j:
                return prefix
            else:
                prefix += i
        return prefix