class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        if len(cost) == 1:
            return 0

        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        print(dp)
        return min(dp[len(cost) - 1] + cost[len(cost) - 1], dp[len(cost) - 2] + cost[len(cost) - 2])