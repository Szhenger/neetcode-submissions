class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        godCnt, queue = 0, deque([(root, float('-inf'))])
        while queue:
            node, pthMax = queue.popleft()
            if node and node.val >= pthMax:
                godCnt += 1
                pthMax = node.val
            if node:
                queue.append((node.left, pthMax))
                queue.append((node.right, pthMax))
        return godCnt
