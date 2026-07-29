# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        stack = [root]
        mp = {None: 0}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                stack.pop()
                maxLeft = mp[node.left]
                maxRight = mp[node.right]
                mp[node] = max(node.val, maxLeft + node.val, maxRight + node.val)
                res = max(mp[node], res, maxLeft + node.val + maxRight)
        return res