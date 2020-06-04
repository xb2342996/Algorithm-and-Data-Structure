## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给出一个完全二叉树，求出该树的节点个数。
'''
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        depth = self.depth(root)
        if depth == 0:
            return 1

        left, right = 1, 2 ** depth - 1
        while left <= right:
            mid = (left + right) // 2
            if self.exits(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1

        return (2 ** depth - 1) + left


    def exits(self, index, depth, node):

        left, right = 0, 2 ** depth - 1
        for _ in range(depth):
            mid = (left + right) // 2
            if index <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

    def depth(self, root):
        depth = 0
        while root.left:
            root = root.left
            depth += 1
        return depth