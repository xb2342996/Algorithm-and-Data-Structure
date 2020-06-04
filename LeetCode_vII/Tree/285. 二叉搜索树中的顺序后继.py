## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给你一个二叉搜索树和其中的某一个结点，请你找出该结点在树中顺序后继的节点。
结点 p 的后继是值比 p.val 大的结点中键值最小的结点。
'''
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.prev = None
        self.succssor = None
        self.inorder(root, p)
        return self.succssor

    def inorder(self, node, p):
        if node is None:
            return

        self.inorder(node.left, p)
        if self.prev and self.succssor is None and self.prev.val == p:
            self.succssor = node
            return

        self.prev = node
        self.inorder(node.right, p)