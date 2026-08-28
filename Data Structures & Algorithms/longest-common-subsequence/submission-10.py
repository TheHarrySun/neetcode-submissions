class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0

        memo = [[-1] * len(text2) for _ in range(len(text1))]

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            curr = 0
            if text1[i] == text2[j]:
                curr = dfs(i + 1, j + 1) + 1            
            curr = max(curr, dfs(i + 1, j), dfs(i, j + 1))

            memo[i][j] = curr
            return curr
        return dfs(0, 0)