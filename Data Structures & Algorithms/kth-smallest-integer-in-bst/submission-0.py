class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index, node, stack = 0, root, []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            index += 1
            if index == k:
                return node.val
            node = node.right




        