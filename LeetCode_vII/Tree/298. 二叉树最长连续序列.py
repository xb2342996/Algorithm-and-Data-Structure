## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode

'''
给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。
该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。
这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。
'''
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = 0
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val != node.val + 1:
                left = 0

            if node.right and node.right.val != node.val + 1:
                right = 0
            max_path = max(left, right) + 1
            self.max_length = max(self.max_length, max_path)
            return max_path


        dfs(root)
        return self.max_length