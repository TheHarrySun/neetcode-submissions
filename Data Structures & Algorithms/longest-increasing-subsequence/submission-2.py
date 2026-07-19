from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        cache = [-1] * len(nums)
        def dfs(i):
            if i == len(nums) - 1:
                return 1
            
            if cache[i] != -1:
                return cache[i]
            
            res = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            
            if res == 0:
                res = 1
            cache[i] = res
            return cache[i]
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans