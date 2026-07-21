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

        # so the logic is that the deque stores tuples of (value, index)
        # the goal is to have it so the deque is monotonically decreasing, because we're moving our sliding window from left to right,
        # so if there is a value that is larger on the right side, then we don't care about the smaller values to the left
        # the maximum will be found by looking at the left side, aka q[0]
        # whenever we add a value to the deque that is larger than the right most value, then we pop from the right until the rightmost
        # value isn't smaller
        # whenever the sliding window moves past the left most value, then we just pop from the left by checking the index