## written by xiongbiao
## date 2020-6-2
from Tree.node import TreeNode
'''
给定一个二叉树，你需要找出二叉树中最长的连续序列路径的长度。
请注意，该路径可以是递增的或者是递减。例如，[1,2,3,4] 和 [4,3,2,1] 都被认为是合法的，而路径 [1,2,4,3] 则不合法。
另一方面，路径可以是 子-父-子 顺序，并不一定是 父-子 顺序。
'''
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs(root)
        return self.ans


    def dfs(self, node):
        res = [1, 1]
        if node is None:
            return res
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if node.left and node.left.val - node.val == 1:
            res[1] = left[1] + 1
        if node.left and node.left.val - node.val == -1:
            res[0] = left[0] + 1

        if node.right and node.right.val - node.val == 1:
            res[1] = max(res[1], right[1] + 1)
        if node.right and node.right.val - node.val == -1:
            res[0] = max(res[0], right[0] + 1)

        self.ans = max(res[0] + res[1] - 1, self.ans)
        return res