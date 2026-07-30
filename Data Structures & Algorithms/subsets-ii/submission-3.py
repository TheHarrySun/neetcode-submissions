class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        ans = []
        def dfs(i):
            if i == len(nums):
                res.append(ans.copy())
                return
            
            ans.append(nums[i])
            dfs(i + 1)
            val = ans.pop()
            while i < len(nums) and nums[i] == val:
                i += 1
            dfs(i)
        dfs(0)
        return res