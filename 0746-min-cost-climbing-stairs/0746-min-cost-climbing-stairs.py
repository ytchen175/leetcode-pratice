class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        
        # eg. [10, 15, 20]
            # local_min = 10, ptr1 = 0, ptr2 = 10
            # local_min = min(0, 10) + 15 = 15, ptr1 = 10, ptr2 = 15
            # local_min = min(10, 15) + 20 = 30, ptr1 = 15, ptr2 = 30
            # return min(15, 30) = 15
        for c in cost:
            local_min = min(ptr1, ptr2) + c
            ptr1 = ptr2
            ptr2 = local_min
            
        return min(ptr1, ptr2)

