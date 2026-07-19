class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        brute force
        res = []
        for i in range(0, len(nums) - k + 1):
            temp_max = float('-infinity')
            for j in range(i, i + k):
                temp_max = max(temp_max, nums[j])
            res.append(temp_max)
        return res
        '''
        # optimal method

        neg_nums = [-num for num in nums]
        heap = []
        heapq.heapify(heap)

        for i in range(k - 1):
            heapq.heappush(heap, (neg_nums[i], i))
        print(heap)
        res = []
        for i in range(0, len(nums) - k + 1):
            print(res)
            l = i
            r = i + k - 1
            heapq.heappush(heap, (neg_nums[r], r))
            while not ((heap[0][1] <= r) and (heap[0][1] >= l)):
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
        return res