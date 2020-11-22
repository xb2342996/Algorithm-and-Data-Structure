# written by xiongbiao
# date 2020-11-22

'''
给你一棵二叉树，请按以下要求的顺序收集它的全部节点：
依次从左到右，每次收集并删除所有的叶子节点
重复如上过程直到整棵树为空
'''
from Tree.node import TreeNode

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        if root is None:
            return []

        self.levels = defaultdict(list)
        self.postOrderTravesal(root)
        ans = []
        for key, value in self.levels.items():
            ans.append(value)
        return ans

    def postOrderTravesal(self, node):
        if node is None:
            return 0

        left = self.postOrderTravesal(node.left)
        right = self.postOrderTravesal(node.right)
        self.levels[max(left, right) + 1].append(node.val)
        return max(left, right) + 1

