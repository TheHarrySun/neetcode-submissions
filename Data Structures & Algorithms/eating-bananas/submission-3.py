from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = 0
        l = 1
        for i in piles:
            r = max(i, r)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for i in piles:
                if i % mid != 0:
                    time += (i // mid) + 1
                else:
                    time += (i // mid)
            if time <= h:
                res = mid
                r = mid - 1
            elif time > h:
                l = mid + 1
        return res
