class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i, j, k):
            if k == len(s3):
                return True if i == len(s1) and j == len(s2) else False
            if j > len(s2):
                return False
            if i > len(s1):
                return False
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans = ans or dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                ans = ans or dfs(i, j + 1, k + 1)
            memo[(i, j, k)] = ans
            return ans
        return dfs(0, 0, 0)