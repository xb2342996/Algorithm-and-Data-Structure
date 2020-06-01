## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode

'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
'''

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        self.flag = True
        self.inorder(root)
        return self.flag

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        if self.prev and root.val < self.prev.val:
            self.flag = False
            return

        self.prev = root
        self.inorder(root.right)

