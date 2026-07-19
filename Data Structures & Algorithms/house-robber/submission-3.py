class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        # recursion method
        def dfs(i):
            if i >= len(nums):
                return 0
            
            return max(nums[i] + dfs(i + 2), dfs(i + 1))
        return max(dfs(0), dfs(1))
        '''

        # botton-up

        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        return max(dfs(0), dfs(1))