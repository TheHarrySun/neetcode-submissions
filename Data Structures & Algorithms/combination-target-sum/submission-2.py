from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        subset = []
        def dfs(i: int):
            if sum(subset) == target:
                ans.append(subset.copy())
                return
            elif sum(subset) > target:
                return
            
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i)
            
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return ans