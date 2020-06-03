## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。
子树是树中的任意节点和它的所有后代构成的集合。
树的平均值是树中节点值的总和除以节点数。
'''
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.max_avg = float('-inf')
        self.postorder(root)
        return self.max_avg

    def postorder(self, node):
        if node is None:
            return 0, 0

        left_sum, left_size = self.postorder(node.left)
        right_sum, right_size = self.postorder(node.right)

        sum = left_sum + right_sum + node.val
        size = left_size + right_size + 1
        self.max_avg = max(self.max_avg, float(sum / size))

        return sum, size