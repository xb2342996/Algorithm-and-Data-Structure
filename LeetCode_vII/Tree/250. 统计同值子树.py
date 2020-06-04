## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个二叉树，统计该二叉树数值相同的子树个数。
同值子树是指该子树的所有节点都拥有相同的数值。
'''
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        def is_same(node):
            if node is None:
                return True

            rightOK = False
            if node.right is None or is_same(node.right) and node.val == node.right.val:
                rightOK = True

            leftOK = False
            if node.left is None or is_same(node.left) and node.val == node.left.val:
                leftOK = True

            if leftOK and rightOK:
                self.count += 1
                return True

            return False

        is_same(root)
        return self.count
