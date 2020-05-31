## written by xiongbiao
## date 2020-5-31
from Tree.node import TreeNode
'''
二叉搜索树中的两个节点被错误地交换。
请在不改变其结构的情况下，恢复这棵树。
'''
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None
        self.find(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def find(self, node):
        if node is None:
            return
        self.find(node.left)
        if self.prev and self.prev.val > node.val:
            self.second = node
            if self.first:
                return
            self.first = self.prev
        self.prev = node
        self.find(node.right)