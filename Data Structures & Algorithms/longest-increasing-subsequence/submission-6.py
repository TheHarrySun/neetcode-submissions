class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, prev):
            if i == n:
                return 0
            if memo[i][prev + 1] != -1:
                return memo[i][prev + 1]

            temp = dfs(i + 1, prev)

            if prev == -1 or nums[prev] < nums[i]:
                temp = max(temp, 1 + dfs(i + 1, i))
            
            memo[i][prev + 1] = temp
            return temp

        return dfs(0, -1)