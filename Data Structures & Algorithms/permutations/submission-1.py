class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], picked: List[bool]):
            if len(curr) == len(nums):
                print(curr)
                res.append(curr.copy())
                return
            
            for i in range(len(picked)):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    backtrack(curr, picked)
                    curr.pop()
                    picked[i] = False
        
        backtrack([], [False] * len(nums))
        return res