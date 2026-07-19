from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        inside = [False] * len(nums)
        ans = []
        def dfs(index, curr):
            if index == len(nums):
                ans.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not inside[i]:
                    curr.append(nums[i])
                    inside[i] = True
                    dfs(index + 1, curr)
                    curr.pop()
                    inside[i] = False
        dfs(0, [])
        return ans