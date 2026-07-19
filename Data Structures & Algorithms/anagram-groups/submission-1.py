class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = str(count)
            if key in word_map:
                word_map[key].append(word)
            else:
                word_map[key] = [word]
        ans = []
        for key, val in word_map.items():
            ans.append(val)
        return ans