class Solution:
    # using a deque for O(n) solution
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0
        r = 0

        while r < len(nums):
            while q and q[-1][0] < nums[r]:
                q.pop()
            q.append((nums[r], r))

            while q[0][1] < l:
                q.popleft()

            if r >= k - 1:
                res.append(q[0][0])
                l += 1
            r += 1
        return res