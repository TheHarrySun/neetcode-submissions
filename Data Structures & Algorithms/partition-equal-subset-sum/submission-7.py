class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2

        memo = [[-1] * (half + 1) for _ in range(len(nums) + 1)]

        def dfs(i, partial):
            if partial == half:
                return True
            if i == len(nums) or partial > half:
                return False
            if memo[i][partial] != -1:
                return True if memo[i][partial] == 1 else False

            ans = False
            for j in range(i + 1, len(nums)):
                ans = ans or dfs(j, partial + nums[j])
            if ans:
                memo[i][partial] = True
            else:
                memo[i][partial] = False
            return ans

        return dfs(0, 0)