class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                ans = max(ans, prices[r] - prices[l])
                r += 1
        return ans