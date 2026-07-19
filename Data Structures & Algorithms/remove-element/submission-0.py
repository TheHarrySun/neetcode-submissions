class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_val = 0
        for i in range(len(nums)):
            if nums[i] == val:
                num_val += 1
        for i in range(num_val):
            nums.remove(val)
        return len(nums)