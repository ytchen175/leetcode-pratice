class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         ptr1, ptr2 = 0, 0
        
#         for c in cost:
#             local_min = min(ptr1 + c, ptr2)
#             ptr1 = ptr2
#             ptr2 = local_min
            
#         return ptr2
        ptr1, ptr2 = 0, 0
        
        for c in cost:
            local_min = min(ptr1, ptr2) + c
            ptr1 = ptr2
            ptr2 = local_min
            
        return min(ptr1, ptr2)