class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        m = 1
        r = len(nums) - 1
        nums = sorted(nums)
        ans = []
        ansset = set()
        while l < len(nums) - 2:
            diff = -nums[l]
            while m < r:
                diff2 = diff - nums[m]
                if nums[r] > diff2:
                    r -= 1
                elif nums[r] < diff2:
                    m += 1
                else:
                    to_append = [nums[l], nums[m], nums[r]]
                    if not str(to_append) in ansset:                    
                        ans.append(to_append)
                        ansset.add(str(to_append))
                    m += 1
                    r -= 1
            l += 1
            m = l + 1
            r = len(nums) - 1
        return ans