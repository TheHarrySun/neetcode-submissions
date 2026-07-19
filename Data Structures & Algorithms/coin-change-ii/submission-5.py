from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = [[-1] * (amount + 1) for _ in range(len(coins))]
        def dfs(i, curr_amt):
            if curr_amt == 0:
                return 1
            if i >= len(coins) or curr_amt < 0:
                return 0
            if cache[i][curr_amt] != -1:
                return cache[i][curr_amt]
            
            cache[i][curr_amt] = dfs(i, curr_amt - coins[i]) + dfs(i + 1, curr_amt)
            return cache[i][curr_amt]
        return dfs(0, amount)