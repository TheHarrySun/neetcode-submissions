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

        layer_traversal = []
        queue = deque([root])
        while queue:
            length = len(queue)
            layer = []
            for _ in range(length):
                node = queue.popleft()

                if not node:
                    continue
                layer.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if layer:
                layer_traversal.append(layer)
            
        for layer in layer_traversal:
            res.append(layer[-1])
        return res