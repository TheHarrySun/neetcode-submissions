from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = [[-1] * len(prices) for _ in range(2)]
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            
            if cache[holding][i] != -1:
                return cache[holding][i]
            
            res = 0
            if holding:
                res = max(res, prices[i] + dfs(i + 2, False), dfs(i + 1, True))
            else:
                res = max(res, -prices[i] + dfs(i + 1, True), dfs(i + 1, False))
            cache[holding][i] = res
            return res
        
        return dfs(0, False)