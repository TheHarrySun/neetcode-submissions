class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 1:
            return intervals

        res = []
        for i in range(0, len(intervals) - 1):
            first = intervals[i]
            second = intervals[i + 1]

            if first[1] < second[0]:
                res.append(first)
            else:
                intervals[i + 1][0] = min(first[0], second[0])
                intervals[i + 1][1] = max(first[1], second[1])
        res.append(intervals[len(intervals) - 1])
        return res