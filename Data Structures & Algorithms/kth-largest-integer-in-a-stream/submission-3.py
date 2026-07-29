class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        heapq.heapify(self.nums)
        for num in nums:
            heapq.heappush(self.nums, num)
        for i in range(len(nums) - k):
            heapq.heappop(self.nums)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        for i in range(len(self.nums) - self.k):
            heapq.heappop(self.nums)
        return self.nums[0]