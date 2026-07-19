from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], index: int, curr: List[int]):
            temp = curr.copy()
            if index == len(nums):
                return [temp]
            temp.append(nums[index])
            ls1 = dfs(nums, index + 1, temp)
            temp.pop()
            ls2 = dfs(nums, index + 1, temp)
            ls1.extend(ls2)
            return ls1
        
        return dfs(nums, 0, [])