class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not node:
                return True
            if lower < node.val < upper:
                return (
                    isValid(node.left, lower, node.val) and 
                    isValid(node.right, node.val, upper)
                )
            return False
        return isValid(root, float('-inf'), float('inf'))

