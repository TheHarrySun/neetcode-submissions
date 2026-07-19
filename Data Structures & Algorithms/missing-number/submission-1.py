from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        total_sum = sum(nums)
        
        new_num = (max_num) * (max_num + 1) // 2 - total_sum
        if new_num == 0 and 0 in nums:
            return max_num + 1
        return new_num