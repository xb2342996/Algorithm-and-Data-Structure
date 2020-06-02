## written by xiongbiao
## date 2020-6-2
from Tree.node import TreeNode

'''
给定一个二叉树，确定它是否是一个完全二叉树。
'''
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        queue.append(root)
        leaf = True
        while queue:
            node = queue.pop(0)
            if not node.left and node.right:
                return False
            elif leaf and not node.right:
                leaf = False
            elif not leaf and (node.left or node.right):
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True