class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sorting 
        intervals.sort(key = lambda x: (x[0], -x[1]))
        i = 1
        while i < len(intervals):
            if intervals[i-1][0] <= intervals[i][0] and intervals[i][1] <= intervals[i-1][1]:
                intervals.pop(i)
            else:
                i += 1
        return len(intervals)