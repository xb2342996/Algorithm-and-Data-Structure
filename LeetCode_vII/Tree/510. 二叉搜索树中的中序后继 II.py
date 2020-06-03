## written by xiongbiao
## date 2020-6-3

'''
给定一棵二叉搜索树和其中的一个节点 node ，找到该节点在树中的中序后继。
如果节点没有中序后继，请返回 null 。
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        node = node.right
        if node:
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.left == node:
            node = node.parent
        return node.parent