class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        ans = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(ans.copy())
                return
            elif curr_sum > target:
                return
            
            if i == len(nums):
                return
            
            ans.append(nums[i])
            val = curr_sum + nums[i]
            dfs(i, val)

            ans.pop()
            val -= nums[i]
            dfs(i + 1, val)
        dfs(0, 0)
        return res