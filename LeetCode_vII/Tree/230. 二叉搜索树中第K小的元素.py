## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.ans = None
        self.inorder(root, k)
        return self.ans

    def inorder(self, node, k):
        if node is None:
            return
        self.inorder(node.left, k)
        if self.count == k:
            self.ans = node.val

        self.count += 1
        self.inorder(node.right, k)