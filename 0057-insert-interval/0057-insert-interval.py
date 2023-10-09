class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # interval[i] 跟 newInterval 沒重疊，newInterval 正好是最小區間
            if intervals[i][0] > newInterval[1]: # eg. [4, 5], [6, 8] / [2, 3] -> [[2, 3], [4, 5], [6, 8]]
                res.append(newInterval)
                return res + intervals[i:] # 已 sorted 所以不會再有重疊了, 直接 append 所有舊 intervals

            # interval[i] 跟 newInterval 沒重疊但 newInterval 不是最小區間
            elif intervals[i][1] < newInterval[0]: # eg. [3, 5] / [6, 8] -> [[3, 5], [6, 8]]
                res.append(intervals[i]) # 以防萬一還是得繼續 traverse

            # interval[i] 跟 newInterval 重疊了，取區間最小值 & 區間最大值做為 newInterval
            else:
                # 不直接 append 進 res 是因為可能還需要 overwrite 掉新的 intervals[i]
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            
        res.append(newInterval)

        return res