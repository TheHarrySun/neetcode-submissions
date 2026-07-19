class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures.copy()
        
        aheads = []
        heapq.heapify(aheads)
        res = []
        while len(temps) != 0:
            top = temps.pop()
            ind = len(temps)
            if len(aheads) == 0:
                heapq.heappush(aheads, (top, ind))
                res.append(0)
            else:
                smallest, index = aheads[0]
                while len(aheads) != 1 and top >= smallest:
                    heapq.heappop(aheads)
                    smallest, index = aheads[0]
                if top >= smallest:
                    if len(aheads) == 1:
                        heapq.heappop(aheads)
                    res.append(0)
                else:
                    res.append(index - ind)
                heapq.heappush(aheads, (top, ind))
        res.reverse()
        return res