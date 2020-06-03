## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
'''

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ans = []
        path = []
        self.dfs(root, path, sum)

    def dfs(self, node, path, rest):

        if rest == 0:
            self.ans.append(path[:])
            return

        rest -= node.val

        path.append(node.val)
        if node.left:
            self.dfs(node.left, path, rest)
            path.pop()

        if node.right:
            self.dfs(node.right, path, rest)
            path.pop()