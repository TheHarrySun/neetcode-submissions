class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        sell_price = prices[0]

        res = 0
        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                res = max(sell_price - buy_price, res)
                buy_price = prices[i]
                sell_price = prices[i]
                continue
            res = max(prices[i] - buy_price, res)
            sell_price = prices[i]
        return res
            