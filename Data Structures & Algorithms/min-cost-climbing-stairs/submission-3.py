from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i):
            if i >= len(cost):
                return 0
            
            return min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))
        
        return min(dfs(0), dfs(1))