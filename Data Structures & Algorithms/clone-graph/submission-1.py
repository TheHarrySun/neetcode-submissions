class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodelst = {}
        visited = []
        def dfs(node, prev):
            if node.val in nodelst.keys():
                return nodelst[node.val]
            new_node = Node(node.val)
            nodelst[node.val] = new_node
            for neighbor in node.neighbors:
                if neighbor.val == prev.val:
                    new_node.neighbors.append(prev)
                    continue
                new_node.neighbors.append(dfs(neighbor, new_node))
            return new_node
        return dfs(node, Node(-1))