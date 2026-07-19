class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heap.append((-nums[i], i))
        
        heapq.heapify(heap)
        res = []
        l = 0
        r = k - 1
        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))
            top = heap[0]
            while not (top[1] <= r and top[1] >= l):
                heapq.heappop(heap)
                top = heap[0]
            res.append(-top[0])
            r += 1
            l += 1
            
        return res