class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return [max(nums)]
        
        res = []

        heap = []
        heapq.heapify(heap)

        l = 0
        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))
        r = k - 1

        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))
            while len(heap) != 0:
                entry = heap[0]
                if entry[1] >= l and entry[1] <= r:
                    res.append(-entry[0])
                    break
                heapq.heappop(heap)
            l += 1
            r += 1
        return res