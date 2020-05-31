## written by xiongbiao
## date 2020-5-31
from Tree.node import TreeNode

'''
给定一个二叉树，我们在树的节点上安装摄像头。
节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
计算监控树的所有节点所需的最小摄像头数量。
'''

class Solution(object):

    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if self.setCamera(root) == 0:
            self.ans += 1
        return self.ans

    def setCamera(self, node):
        if not node:
            return 1

        left = self.setCamera(node.left)
        right = self.setCamera(node.right)

        if left == 0 or right == 0:
            self.ans += 1
            return 2

        if left == 1 and right == 1:
            return 0

        if left + right >= 3:
            return 1

        return -1


    '''
    后续遍历 + 动态规划
    '''
    # def minCameraCover(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #
    #     def solve(node):
    #         if node is None:
    #             return 0, 0, float('inf')
    #
    #         l = solve(node.left)
    #         r = solve(node.right)
    #
    #         dp0 = l[1] + r[1]
    #         dp1 = min(l[2] + min(r[1:]), r[2] + min(l[1:]))
    #         dp2 = 1 + min(l) + min(r)
    #
    #         return dp0, dp1, dp2
    #
    #     return min(solve(root))