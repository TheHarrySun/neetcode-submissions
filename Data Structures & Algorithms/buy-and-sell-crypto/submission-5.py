class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0

        res = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                res = max(prices[r] - prices[l], res)
                l = i
                r = i
                continue
            elif prices[i] >= prices[r]:
                r = i
        return max(prices[r] - prices[l], res)