class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix and suffix sums; this is one way, but let's try doing it with just one variable
        '''
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left_prod[i] *= left_prod[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right_prod[i] *= right_prod[i + 1] * nums[i + 1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left_prod[i] * right_prod[i]
        return res
        '''
        res = [1] * len(nums)
        prefix = 1
        
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res