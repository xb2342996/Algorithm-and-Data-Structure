## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。
'''

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == target and root.left is None and root.right is None:
            return None
        self.dfs(root, None, target)
        return root


    def dfs(self, node, parent, target):
        if node.left is None and node.right is None:
            if node.val == target:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

        if node.left:
            self.dfs(node.left, node, target)
        if node.right:
            self.dfs(node.right, node, target)

        if node.left is None and node.right is None and node.val == target and parent:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None