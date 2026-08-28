class Solution:   
    def isSame(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node: continue
            if self.isSame(node, subRoot): return True
            queue.append(node.left)
            queue.append(node.right)
        return False
