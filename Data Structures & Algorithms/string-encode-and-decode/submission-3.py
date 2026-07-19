class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word)) + '#' + word
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while (i < len(s)):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = j + length + 1
            ans.append(s[i:j])
            i = j
        return ans