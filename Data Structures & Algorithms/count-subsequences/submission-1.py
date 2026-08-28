class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = 0
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)
            ans += dfs(i + 1, j)

            memo[(i, j)] = ans
            return ans
        
        return dfs(0, 0)