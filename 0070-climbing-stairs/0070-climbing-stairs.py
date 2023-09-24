class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 2 # n = 1 & n = 2 answer
        steps = 0
        
        arr = [prev1, prev2] # preset known answers
        
        for i in range(2, n): # start DP from unknown ans
            prev1, prev2 = arr[-1], arr[-2]
            steps = prev1 + prev2
            
            arr.append(steps) # store ans
        
        return arr[n - 1] # get newest ans