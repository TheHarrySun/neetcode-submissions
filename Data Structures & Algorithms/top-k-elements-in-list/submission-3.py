class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for key, val in counts.items():
            freq[val].append(key)
        
        ans = []
        for i in range(len(nums), 0, -1):
            if k == 0:
                break
            for num in freq[i]:
                ans.append(num)
                k -= 1
        return ans