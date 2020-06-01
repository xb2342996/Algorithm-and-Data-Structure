## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode

'''
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
'''
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        new_min = 0
        for node in preorder:
            if new_min > node:
                return False
            while stack and node > stack[-1]:
                new_min = stack.pop()
            stack.append(node)
        return True