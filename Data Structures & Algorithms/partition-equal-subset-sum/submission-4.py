from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        
        cache = [[-1] * (target + 1) for _ in range(len(nums))]
        def dfs(i, curr_target):
            if curr_target == 0:
                return True
            
            if i == len(nums):
                return False
            
            if cache[i][curr_target] != -1:
                return cache[i][curr_target]
            
            cache[i][curr_target] = dfs(i + 1, curr_target) or dfs(i + 1, curr_target - nums[i])
            return cache[i][curr_target]
        
        return dfs(0, target)