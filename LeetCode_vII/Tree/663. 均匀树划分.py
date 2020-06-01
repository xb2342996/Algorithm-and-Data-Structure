## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode

'''
给定一棵有 n 个结点的二叉树，你的任务是检查是否可以通过去掉树上的一条边将树分成两棵，且这两棵树结点之和相等。
'''

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.total_sum = []
        self.postorder(root)
        print(self.total_sum)
        total = self.total_sum[-1]
        return True if total / 2 in self.total_sum else False

    def postorder(self, node):
        if node is None:
            return 0

        left_sum = self.postorder(node.left)
        right_sum = self.postorder(node.right)
        val = left_sum + right_sum + node.val
        self.total_sum.append(val)
        return val