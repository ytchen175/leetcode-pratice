class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._min_heap = nums
        self._k = k
        
        heapq.heapify(self._min_heap)

        while (len(self._min_heap) > k):
            heapq.heappop(self._min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self._min_heap, val)

        if len(self._min_heap) > self._k:
            while (len(self._min_heap) > self._k):
                heapq.heappop(self._min_heap)
        return self._min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)