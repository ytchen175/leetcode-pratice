class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = [] # declare subset as global var to prevent some annoying problem

        def dfs(i): # index: 0, 1, 2
            if i >= len(nums):
                results.append(subset.copy())
                return
            else:
                # 不斷的把 nums[i] 加進來, 也就是左邊的 sub tree
                subset.append(nums[i])
                dfs(i + 1)

                # 不斷的不把 nums[i] 加進來, 也就是右邊的 sub tree
                subset.pop()
                dfs(i + 1)
        
        dfs(0) # set index=0 as start point
        return results