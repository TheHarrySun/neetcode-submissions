from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache1 = [-1] * (len(nums) - 1)
        cache2 = [-1] * (len(nums) - 1)
        def dfs(i, houses, cache):
            if i >= len(houses):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(houses[i] + dfs(i + 2, houses, cache), dfs(i + 1, houses, cache))
            return cache[i]
        
        return max(dfs(0, nums[:len(nums) - 1], cache1), dfs(0, nums[1:], cache2))