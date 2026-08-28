class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        memo = [[-1] * (2 * total + 1) for _ in range(len(nums))]

        def dfs(i, curr):
            if curr == target and i == len(nums):
                return 1
            elif i == len(nums):
                return 0

            idx = curr + total

            if memo[i][idx] != -1:
                return memo[i][idx]
            
            memo[i][idx] = dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
            return memo[i][idx]
        return dfs(0, 0)