class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        ans = []
        pick = [False] * len(nums)
        def dfs():
            if len(ans) == len(nums):
                res.append(ans.copy())
            
            for i in range(len(nums)):
                if not pick[i]:
                    ans.append(nums[i])
                    pick[i] = True
                    dfs()
                    ans.pop()
                    pick[i] = False

        dfs()
        return res