class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = [[-1] * len(text2) for _ in range(len(text1))]
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            res = 0
            if text1[i] == text2[j]:
                res = max(res, 1 + dfs(i + 1, j + 1))
            
            res = max(res, dfs(i + 1, j), dfs(i, j + 1))
            cache[i][j] = res
            
            return res
        return dfs(0, 0)
