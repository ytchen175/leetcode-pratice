class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 2 # n=1 & n=2 answer
        curr = 0
        
        arr = [prev1, prev2]
        
        for i in range(2, n):
            prev1, prev2 = arr[-1], arr[-2]
            curr = prev1 + prev2
            
            arr.append(curr)
        
        return arr[n-1]