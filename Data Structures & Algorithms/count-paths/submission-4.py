class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                memo[m - 1][n - 1] = 1
                return 1
            if memo[x][y] != -1:
                return memo[x][y]

            if x == m - 1:
                memo[x][y] = dfs(x, y + 1)
            elif y == n - 1:
                memo[x][y] = dfs(x + 1, y)
            else:
                memo[x][y] = dfs(x, y + 1) + dfs(x + 1, y)
            return memo[x][y]
        return dfs(0, 0)