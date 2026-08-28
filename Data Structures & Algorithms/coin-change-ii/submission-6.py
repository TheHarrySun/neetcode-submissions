class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(i, curr):
            if curr == amount:
                return 1
            if curr > amount:
                return 0
            if i == len(coins):
                return 0
            if memo[i][curr] != -1:
                return memo[i][curr]
            
            memo[i][curr] = dfs(i, curr + coins[i]) + dfs(i + 1, curr)
            return memo[i][curr]
        return dfs(0, 0)