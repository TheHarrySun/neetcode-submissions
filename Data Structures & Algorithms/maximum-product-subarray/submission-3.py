from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        
        res = -float('infinity')
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - i - 1] * (suffix or 1)
            res = max(res, max(prefix, suffix))
            
        return res