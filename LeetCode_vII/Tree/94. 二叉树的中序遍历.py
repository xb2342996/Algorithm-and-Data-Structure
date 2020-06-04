## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个二叉树，返回它的 中序 遍历。
'''


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, ans = [], []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right

        return ans
