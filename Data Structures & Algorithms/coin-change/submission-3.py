from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = [-1] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                cache[coin] = 1
        
        def dfs(i):
            if i < 0:
                return float('infinity')
            if cache[i] != -1:
                return cache[i]
            
            res = float('infinity')
            for coin in coins:
                if coin <= amount:
                    res = min(res, 1 + dfs(i - coin))
            cache[i] = res
            return cache[i]
        
        return dfs(amount) if dfs(amount) != float('infinity') else -1