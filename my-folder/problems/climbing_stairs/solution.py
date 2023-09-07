class Solution:
    def climbStairs(self, n: int) -> int:
        # stairs: 1 2 3 4...
        # sols: 1 2 3 5...
        prev1 = 1 # set as arr[0]
        prev2 = 2 # set as arr[1]
        curr = 0
        
        sol = [prev1, prev2]

        if n <= 2:
            return n
        else:
            for i in range(2, n): # start DP
                prev1, prev2 = sol[-2], sol[-1]
                curr = prev1 + prev2
                sol.append(curr) # save result 

        return curr
                