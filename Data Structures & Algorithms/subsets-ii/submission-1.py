class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i: int, curr: List[int]):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr_val = curr.pop()
            while i < len(nums) and nums[i] == curr_val:
                i += 1
            backtrack(i, curr)
        backtrack(0, [])
        return res