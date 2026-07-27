# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        mp = {root: root.val}
        queue = deque([root])

        res = 0
        while queue:
            node = queue.popleft()
            if node.val >= mp[node]:
                res += 1
            
            if node.left:
                mp[node.left] = max(mp[node], node.left.val)
                queue.append(node.left)
            if node.right:
                mp[node.right] = max(mp[node], node.right.val)
                queue.append(node.right)
        return res