class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            elif i >= len(candidates) or total > target:
                return
            else:
                # 選擇加 i
                curr.append(candidates[i])
                dfs(i, curr, total + candidates[i])

                # 選擇不加 i
                curr.pop()
                dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res