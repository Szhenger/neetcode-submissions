class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base case
        if not node:
            return None
        clone, queue = { node : Node(node.val) }, deque([node])
        # Breadth-first search
        while queue:
            vertex = queue.popleft()
            for neighbor in vertex.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone[vertex].neighbors.append(clone[neighbor])
        return clone[node] 
        