## written by xiongbiao
## date 2020-5-31
from Tree.node import TreeNode
'''
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。
'''
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.nodes = []
        self.findNode(root)
        print(self.nodes)

        left = 0
        right = len(self.nodes) - k
        while left < right:
            mid = (left + right) >> 1
            if target - self.nodes[mid] <= self.nodes[mid + k] - target:
                right = mid
            else:
                left = mid + 1
        return self.nodes[left:left+k]

    def findNode(self, node):
        if node is None:
            return

        self.findNode(node.left)
        self.nodes.append(node.val)
        self.findNode(node.right)