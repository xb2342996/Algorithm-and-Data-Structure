## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
'''

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.ans = 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node, num):
        num = num * 10 + node.val
        if node.left is None and node.right is None:
            self.ans += num
            return

        if node.left:
            self.dfs(node.left, num)

        if node.right:
            self.dfs(node.right, num)
