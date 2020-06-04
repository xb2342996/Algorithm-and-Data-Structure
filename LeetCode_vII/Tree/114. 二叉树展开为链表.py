## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个二叉树，原地将它展开为一个单链表。
'''
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left is None:
                root = root.right
            else:
                right = root.left
                while right:
                    right = right.right
                right.right = root.right

                root.right = root.left
                root.left = None
                root = root.right
