class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            if not node:
                return True
            return (
                lower < node.val < upper and
                isValid(node.left, lower, node.val) and 
                isValid(node.right, node.val, upper)
                )
        return isValid(root, float('-inf'), float('inf'))

