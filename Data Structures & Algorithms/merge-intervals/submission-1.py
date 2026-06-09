class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda p: p[0])

        output = [intervals[0]]

        for start, end in intervals:
            endtime = output[-1][1]

            if endtime >= start:
                output[-1][1] = max(endtime, end) 
            else:
                output.append([start, end])
        return output
        
        