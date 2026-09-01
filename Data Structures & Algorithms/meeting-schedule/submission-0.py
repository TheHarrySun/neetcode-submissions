"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_list = []
        for interval in intervals:
            intervals_list.append((interval.start, interval.end))
        intervals_list.sort()
        for i in range(0, len(intervals_list) - 1):
            first = intervals_list[i]
            second = intervals_list[i + 1]
            if first[1] > second[0]:
                return False
        return True