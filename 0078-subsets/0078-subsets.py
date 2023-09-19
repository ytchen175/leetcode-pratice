class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = [] # declare subset as global var to prevent some annoying problem
        
        def dfs(i): # index: 0, 1, 2
            if i >= len(nums):
                res.append(subset.copy())
                return
            else:
                # left subtree, add nums[i]
                subset.append(nums[i])
                dfs(i + 1)

                # right subtree, don't add nums[i]
                subset.pop()
                dfs(i + 1)

        dfs(0) # entry point

        return res