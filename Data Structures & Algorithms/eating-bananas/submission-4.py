class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        ans = 0
        while l <= r:
            m = l + (r - l) // 2

            time = 0
            for pile in piles:
                time += -(-pile // m)
            if time <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans