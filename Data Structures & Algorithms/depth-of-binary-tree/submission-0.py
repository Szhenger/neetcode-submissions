class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            return 1 + max(left, right)
        return dfs(root)