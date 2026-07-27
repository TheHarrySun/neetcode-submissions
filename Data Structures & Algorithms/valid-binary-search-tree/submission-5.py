# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-infinity"), float("infinity"))])

        while queue:
            node, leftBound, rightBound = queue.popleft()
            if not node:
                continue
            if node.left and (node.left.val <= leftBound or node.left.val >= node.val):
                return False
            if node.right and (node.right.val >= rightBound or node.right.val <= node.val):
                return False
            
            queue.append((node.left, leftBound, node.val))
            queue.append((node.right, node.val, rightBound))
        return True