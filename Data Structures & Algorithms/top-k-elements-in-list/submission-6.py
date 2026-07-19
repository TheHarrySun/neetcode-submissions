class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        hashmap = {}
        for entry in nums:
            hashmap[entry] = 1 + hashmap.get(entry, 0)
        
        for key, val in hashmap.items():
            freq[val].append(key)

        counter = k
        res = []
        for i in range(len(nums), 0, -1):
            if counter == 0:
                return res
            while freq[i]:
                res.append(freq[i].pop())
                counter -= 1
                if counter == 0:
                    return res
        return res