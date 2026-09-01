class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns = newInterval[0]
        ne = newInterval[1]
        
        res = []
        added = False
        for i, interval in enumerate(intervals):
            s = interval[0]
            e = interval[1]
            if e < ns:
                res.append(interval)
                continue
            if s > ne:
                res.append([ns, ne])
                res += intervals[i:]
                added = True
                break
            ns = min(s, ns)
            ne = max(e, ne)
        if not added:
            res.append([ns, ne])
        return res