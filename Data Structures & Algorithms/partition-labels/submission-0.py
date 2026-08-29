class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i
        
        idx = 0
        res = []
        print(first)
        print(last)
        while idx < len(s):
            print(idx)
            first_sub = idx
            last_sub = last[s[idx]]
            for key, val in first.items():
                if key != s[idx] and val > first_sub and val < last_sub:
                    last_sub = max(last[key], last_sub)
            res.append(last_sub - first_sub + 1)
            idx = last_sub + 1
        return res