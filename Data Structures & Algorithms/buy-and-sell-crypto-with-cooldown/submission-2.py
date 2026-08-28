class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = [[-1] * 2 for _ in range(len(prices))]

        def dfs(bought, time):
            print(bought, time)
            if time >= len(prices):
                return 0
            if memo[time][bought] != -1:
                return memo[time][bought]
            if bought == 0:
                ans = max(dfs(0, time + 1), dfs(1, time + 1) - prices[time])
            elif bought == 1:
                ans = max(dfs(1, time + 1), dfs(0, time + 2) + prices[time])
            print(ans)
            memo[time][bought] = ans
            return ans
        return dfs(0, 0)