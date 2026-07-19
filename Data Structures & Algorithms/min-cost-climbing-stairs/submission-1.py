class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dfs(i, curr_cost):
            if i >= n:
                return curr_cost
            
            curr_cost += cost[i]
            return min(dfs(i + 1, curr_cost), dfs(i + 2, curr_cost))
        return min(dfs(0, 0), dfs(1, 0))