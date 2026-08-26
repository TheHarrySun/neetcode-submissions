class Solution:
    def numDecodings(self, s: str) -> int:
        tens = ['1', '2']
        possible_ones = ['0', '1', '2', '3', '4', '5', '6']

        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] not in tens:
                    return 0
                dp[i] = dp[i - 2] if i - 2 >= 0 else 1
            else:
                dp[i] = dp[i - 1]
                if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] in possible_ones):
                    dp[i] += dp[i - 2] if i - 2 >= 0 else 1
        return dp[n - 1]