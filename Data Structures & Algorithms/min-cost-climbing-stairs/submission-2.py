class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        # Recursion brute-force
        n = len(cost)

        def dfs(i, curr_cost):
            if i >= n:
                return curr_cost
            
            curr_cost += cost[i]
            return min(dfs(i + 1, curr_cost), dfs(i + 2, curr_cost))
        return min(dfs(0, 0), dfs(1, 0))
        '''

        # Bottom-up
        n = len(cost)
        cache = [-1] * n
        def dfs(i):
            print("start", i)
            if i >= n:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[i]
        return min(dfs(0), dfs(1))