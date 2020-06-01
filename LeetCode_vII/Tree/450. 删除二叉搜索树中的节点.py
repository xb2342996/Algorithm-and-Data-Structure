## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode

'''
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。
'''
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node, parent = self.getNode(key, root)
        if node is None:
            return root

        if node.left and node.right:
            replace, re_parent = self.predecessor(node)
            if replace is None:
                replace, re_parent = self.successor(node)
            node.val = replace.val
            node = replace
            parent = re_parent

        if node.left:
            child = node.left
        else:
            child = node.right

        if child:
            if parent.left == node:
                parent.left = child
            elif parent.right == node:
                parent.right = child
            else:
                root = child
        elif parent is None:
            root = None
        else:
            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None

        return root

    def getNode(self, value, root):
        node = root
        while node:
            parent = node
            if node.val > value:
                node = node.left
            elif node.val < value:
                node = node.right
            else:
                return node, parent
        return None, None

    def successor(self, node):
        child = node.right
        if child is None:
            return None, None
        parent = node
        while child and child.left:
            parent = child
            child = child.left
        return parent, child

    def predecessor(self, node):
        child = node.left
        if child is None:
            return None, None
        parent = node
        while child and child.right:
            parent = child
            child = child.right
        return parent, child