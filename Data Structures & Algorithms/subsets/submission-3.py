import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, ans):
            if i == len(nums):
                res.append(ans)
                return
            
            ans1 = copy.deepcopy(ans)
            dfs(i + 1, ans1)
            ans2 = copy.deepcopy(ans)
            ans2.append(nums[i])
            dfs(i + 1, ans2)
            return
        
        dfs(0, [])
        return res