class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for entry in strs:
            hashmap = [0] * 26
            for char in entry:
                hashmap[ord(char) - ord('a')] += 1
            res[tuple(hashmap)].append(entry)
        return list(res.values())