class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l <= 1 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if resLen < r - l + 1:
                        resIdx = l
                        resLen = r - l + 1
        
        return s[resIdx: resIdx + resLen]