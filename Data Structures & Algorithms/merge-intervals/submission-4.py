class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []

        intervals.sort(key = lambda p: p[0])

        res = [intervals[0]]

        for start, end in intervals:
            endtime = res[-1][1] 

            if endtime >= start:
                res[-1][1] = max(endtime, end)
            else:
                res.append([start, end])
        
        return res

        