class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()

        prevEnd = intervals[0][1]
        ans = 0
        for i in range(1, n):
            curr = intervals[i]
            if curr[0] >= prevEnd:
                prevEnd = curr[1]
                continue
            ans += 1
            prevEnd = min(prevEnd, curr[1])
        return ans