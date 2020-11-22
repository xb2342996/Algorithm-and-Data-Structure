# wirtten by xiongbiao
# date 2020-10-21

from Tree.node import TreeNode


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.ans = 0
        self.postOrder(root)
        return self.ans

    def postOrder(self, node):
        if node is None:
            return 0

        left = self.postOrder(node.left)
        right = self.postOrder(node.right)
        self.ans += abs(left - right)
        return left + right + node.val

