class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node: continue
            if self.sameTree(node, subRoot): return True
            queue.append(node.left)
            queue.append(node.right)
        return False
    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
