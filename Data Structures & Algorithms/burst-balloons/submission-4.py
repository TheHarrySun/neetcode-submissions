class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)

        memo = {}

        def dfs(l, r):

            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            ans = 0
            for i in range(l, r + 1):
                ans = max(ans, nums[i] * nums[l - 1] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r))
            memo[(l, r)] = ans
            return ans
        return dfs(1, len(nums) - 2)