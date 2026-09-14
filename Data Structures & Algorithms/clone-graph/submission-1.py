class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge case
        if not node:
            return None
        # Breadth-first search
        clone, queue = { node : Node(node.val) }, deque([node])
        while queue:
            vertex = queue.popleft()
            for neighbor in vertex.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone[vertex].neighbors.append(clone[neighbor])
        return clone[node] 
        