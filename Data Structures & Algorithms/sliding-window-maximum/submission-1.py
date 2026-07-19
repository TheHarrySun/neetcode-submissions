class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        brute force
        '''
        res = []
        for i in range(0, len(nums) - k + 1):
            temp_max = float('-infinity')
            for j in range(i, i + k):
                temp_max = max(temp_max, nums[j])
            res.append(temp_max)
        return res