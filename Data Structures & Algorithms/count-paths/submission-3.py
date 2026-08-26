class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        for i in range(1, m + n - 1):
            ans *= i
        for i in range(1, m):
            ans //= i
        for i in range(1, n):
            ans //= i
        return ans