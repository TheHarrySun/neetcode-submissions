from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        subset = []
        def dfs(i: int, total: int):
            if total == target:
                ans.append(subset.copy())
                return
            elif total > target:
                return
            
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            total += nums[i]
            dfs(i, total)
            
            subset.pop()
            total -= nums[i]
            dfs(i + 1, total)
        dfs(0, 0)
        return ans