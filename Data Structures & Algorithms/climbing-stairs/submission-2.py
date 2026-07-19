class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # Bottom-up method
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = [0] * (n + 1)
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]
        '''

        # Top-down method
        cache = [-1] * (n + 1)

        def dfs(i):
            if i >= n:
                return 1 if i == n else 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)