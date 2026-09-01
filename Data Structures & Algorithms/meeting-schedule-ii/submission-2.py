"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        count = 0
        res = 0
        starts.sort()
        ends.sort()
        s = 0
        e = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                count += 1
                res = max(count, res)
            else:
                e += 1
                count -= 1
        return res