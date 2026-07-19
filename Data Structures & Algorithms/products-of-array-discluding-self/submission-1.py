class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)
        left_prods = [1] * len(nums)
        right_prods = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            left_prods[i] *= left_prods[i - 1] * nums[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            right_prods[i] *= right_prods[i + 1] * nums[i + 1]
        
        for i in range(len(prods)):
            prods[i] *= left_prods[i] * right_prods[i]
        return prods