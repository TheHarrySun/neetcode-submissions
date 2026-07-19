class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)
        def dfs(l, r, cache):
            if l >= r:
                return 0
            
            if cache[l] != -1:
                return cache[l]
            
            cache[l] = max(nums[l] + dfs(l + 2, r, cache), dfs(l + 1, r, cache))
            return cache[l]
        
        return max(dfs(0, len(nums) - 1, cache1), dfs(1, len(nums), cache2))