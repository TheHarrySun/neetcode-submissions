class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-num for num in nums]
        heapq.heapify(neg_nums)
        for _ in range(k - 1):
            heapq.heappop(neg_nums)
        return -neg_nums[0]
        