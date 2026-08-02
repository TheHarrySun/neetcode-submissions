class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            if j == len(word):
                return node.word
            
            curr = node
            ans = False
            if word[j] == ".":
                for key, val in curr.children.items():
                    ans = ans or dfs(j + 1, val)
            elif word[j] in curr.children:
                ans = ans or dfs(j + 1, curr.children[word[j]])
            return ans
        return dfs(0, self.root)