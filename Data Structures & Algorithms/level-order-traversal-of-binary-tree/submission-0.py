class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                levels.append(level)
        return levels
