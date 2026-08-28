class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def dfs(node: TreeNode) -> None:
            if node.left and node.right:
                node.left, node.right = node.right, node.left
                dfs(node.left)
                dfs(node.right)
            elif node.left:
                node.left, node.right = None, node.left
                dfs(node.right)
            elif node.right:
                node.left, node.right = node.right, None
                dfs(node.left)
        dfs(root)
        return root
                
