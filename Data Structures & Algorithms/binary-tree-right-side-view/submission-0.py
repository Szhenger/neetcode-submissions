class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sideView, queue = [], deque([root])
        if not root:
            return sideView
        while queue:
            for _ in range(len(queue) - 1):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            last = queue.popleft()
            sideView.append(last.val)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        return sideView 
            