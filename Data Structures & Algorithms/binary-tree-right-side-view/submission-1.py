class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sideView, queue = [], deque([root])
        while queue:
            last = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    last = node
                    queue.append(node.left)
                    queue.append(node.right)
            if last:
                sideView.append(last.val)    
        return sideView 
            