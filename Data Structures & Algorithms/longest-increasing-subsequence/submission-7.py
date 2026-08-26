class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            temp = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    temp = max(temp, 1 + dfs(j))
            
            memo[i] = temp
            return temp
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans