class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total / 2

        def dfs(i, partial):
            if partial == half:
                return True
            if i == len(nums) or partial > half:
                return False

            ans = False
            for j in range(i + 1, len(nums)):
                ans = ans or dfs(j, partial + nums[j])
            return ans

        return dfs(0, 0)