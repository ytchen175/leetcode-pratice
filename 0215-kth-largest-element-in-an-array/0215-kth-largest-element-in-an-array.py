class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap,-num) # 因為 heapq 的預設是 min heap，所以這邊存進去的時候要加負號
        
        while k > 0:
            res = heapq.heappop(heap) # pop 出來
            k -=1

        return -res # pop 出來時要再加回去

