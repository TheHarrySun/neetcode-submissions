from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(prices) - 1:
            if prices[r] < prices[r + 1]:
                r += 1
            else:
                res = max(prices[r] - prices[l], res)
                if prices[r + 1] < prices[l]:
                    l = r + 1
                r += 1
        return max(res, prices[r] - prices[l])