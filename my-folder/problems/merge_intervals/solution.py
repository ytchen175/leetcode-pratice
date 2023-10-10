class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # adaptive merge sort, O(nlogn)

        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_element = res[-1]

            # eg. [1, 4], [3, 5] -> [1, 5]
            if last_element[1] >= start: 
                last_element[1] = max(last_element[1], end) # update new interval end
            
            # eg. [1, 2], [3, 4]
            else:
                res.append([start, end])
        
        return res