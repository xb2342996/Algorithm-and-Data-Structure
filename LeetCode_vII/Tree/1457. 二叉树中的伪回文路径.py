## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。
请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。
'''
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node, bit):
        bit = bit ^ (1 << node.val)
        if node.left is None and node.right is None:
            if bit == 0 or bit & (bit - 1) == 0:
                self.ans += 1
            return

        if node.left:
            self.dfs(node.left, bit)

        if node.right:
            self.dfs(node.right, bit)