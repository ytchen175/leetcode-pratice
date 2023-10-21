# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k # quickSelect 會讓第 k 個 largest 的元素放在 len(nums) - k 的地方

#         def quickSelect(l, r):
#             rand = random.randint(l, r)
#             nums[rand], nums[r] = nums[r], nums[rand]

#             pivot, p = nums[r], l # 設定 pivot 為 nums[r]，可以想成最右邊較好理解

#             for i in range(l, r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p] # 小於等於 pivot 的 i 跟 p 交換位置
#                     p += 1 # p 前進一格

#             nums[p], nums[r] = nums[r], nums[p] # 最後 pivot(nums[r]) 跟 p 再交換

#             if p > k:
#                 return quickSelect(l, p - 1) # 繼續在左邊尋找
#             elif p < k:
#                 return quickSelect(p + 1, r) # 繼續在右邊尋找
#             else:
#                 return nums[p] # 正好是要找的第 k 個 largest 元素

#         return quickSelect(0, len(nums) - 1)

# from heapq import heapify, heappush, heappushpop
# class Solution: ## complexity nlogk
#     def findKthLargest(self, nums: List[int], k: int) -> int:            
#         x = nums[:k]              
#         heapify(x)
        
#         while(len(nums) > k):
#             heappushpop(x, nums[k])            
#             k += 1
#         return x[0]

# from heapq import heappush, heappop

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         pq = []
#         for i in range(k):
#             heappush(pq, nums[i])
        
#         for i in range(k, len(nums)):
#             if pq[0] < nums[i]:
#                 heappop(pq)
#                 heappush(pq, nums[i])
        
#         return heappop(pq)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        while k > 0:
            res = heapq.heappop(heap)
            k -=1
        return -res
