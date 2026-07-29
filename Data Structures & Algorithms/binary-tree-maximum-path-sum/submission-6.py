# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # the logic goes as follows
    # do DFS, and if we reach a singular node, then the max path containing this node would be its value
    # if we reach a node with children, we store the max value it can have and continue on as a path
    # in other words, if a path were to grow from it and go above, then the node must be either the value of
    # itself, itself plus the max path of its left child, or itself plust he max path of its right child
    # then we also update res to be compared to max path of left child, max path of right child, and the node bc that
    # corresponds to a full path that is possible, and compare that to the map value as well
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