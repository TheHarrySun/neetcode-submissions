from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(i, curr):
            if i == len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])            
            dfs(i + 1, curr)
            
            curr.pop()
            curr_val = nums[i]
            while i < len(nums) and curr_val == nums[i]:
                i += 1
            dfs(i, curr)
        
        dfs(0, [])
        return ans