## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
完全二叉树是每一层（除最后一层外）都是完全填充（即，结点数达到最大）的，并且所有的结点都尽可能地集中在左侧。
设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：
CBTInserter(TreeNode root) 使用头结点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v) 将 TreeNode 插入到存在值为 node.val = v  的树中以使其保持完全二叉树的状态，并返回插入的 TreeNode 的父结点的值；
CBTInserter.get_root() 将返回树的头结点。
'''

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.queue = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left is None or node.right is None:
                self.queue.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        parent = self.queue[0]
        self.queue.append(node)
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.queue.pop(0)
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root