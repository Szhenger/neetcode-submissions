class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter

        