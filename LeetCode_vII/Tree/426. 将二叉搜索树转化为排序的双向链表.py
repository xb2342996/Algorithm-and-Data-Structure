## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。
对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
'''
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        self.prev = None
        self.new_root = None
        self.inorder(root)
        self.prev.right = self.new_root
        self.new_root.left = self.prev
        return self.new_root

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        if self.prev:
            self.prev.right = node
            node.left = self.prev
        else:
            self.new_root = node

        self.prev = node
        self.inorder(node.right)