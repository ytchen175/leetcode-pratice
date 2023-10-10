class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # O(nlogn)

        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_element = res[-1]

            if last_element[1] >= start: # eg. [1, 4], [3, 5] -> [1, 5]
                last_element[1] = max(last_element[1], end)
            else:
                res.append([start, end]) # eg. [1, 2], [3, 4]
        
        return res