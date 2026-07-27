# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        queue = deque([root])
        while queue:
            length = len(queue)
            rightSide = None
            for _ in range(length):
                node = queue.popleft()

                if not node:
                    continue
                rightSide = node.val
                queue.append(node.left)
                queue.append(node.right)
            if rightSide:
                res.append(rightSide)
        return res