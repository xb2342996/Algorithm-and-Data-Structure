## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。
一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
'''

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        from collections import defaultdict
        self.treeSum = defaultdict()
        self.nodeSum(root)
        ans = []
        for key, value in self.treeSum.items():
            if value == max(self.treeSum.values()):
                ans.append(key)

        return ans

    def nodeSum(self, node):
        if node is None:
            return 0

        left = self.nodeSum(node.left)
        right = self.nodeSum(node.right)
        node_sum = left + right + node.val
        self.treeSum[node_sum] += 1
        return node_sum

