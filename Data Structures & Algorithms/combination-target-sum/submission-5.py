class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        nums.sort()

        ans = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(ans.copy())
                return
            elif curr_sum > target:
                return
            
            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                if curr_sum + nums[j] > target:
                    return
                ans.append(nums[j])
                val = curr_sum + nums[j]

                dfs(j, val)
                ans.pop()
                val -= nums[j]
        dfs(0, 0)
        return res