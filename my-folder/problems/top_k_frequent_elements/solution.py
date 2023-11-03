class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()
        res = []
        
        for n in nums:
            if n not in count_dict:
                count_dict[n] = 1
            else:
                count_dict[n] += 1

        sorted_count_dict = dict(
            sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        )
        res = list(sorted_count_dict.keys())

        return res[:k]