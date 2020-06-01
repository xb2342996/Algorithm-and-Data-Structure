## written by xiongbiao
## date 2020-6-1

from Tree.node import TreeNode

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.sums = 0
        self.max = 0

        self.postorder(root)
        self.postorderProduct(root)
        print(self.max)


    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.sums += node.val

    def postorderProduct(self, node):
        if node is None:
            return 0

        left = self.postorderProduct(node.left)
        right = self.postorderProduct(node.right)

        res = left + right + node.val
        self.max = max(self.max, (self.sums - res) * res)
        return res


