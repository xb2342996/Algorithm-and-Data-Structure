## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个二叉树，返回它的 前序 遍历。
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans

    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     self.tree = []
    #     def preorder(node):
    #         if node is None:
    #             return
    #         self.tree.append(node.val)
    #         preorder(node.left)
    #         preorder(node.right)
    #
    #     preorder(root)
    #     return self.tree
