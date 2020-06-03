## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode

'''
给定一个根为 root 的二叉树，每个结点的深度是它到根的最短距离。
如果一个结点在整个树的任意结点之间具有最大的深度，则该结点是最深的。
一个结点的子树是该结点加上它的所有后代的集合。
'''
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        def dfs(node):
            if node is None:
                return 0, None

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth == right_depth:
                root = node
            elif left_depth > right_depth:
                root = left_node
            else:
                root = right_node

            return 1 + max(left_depth, right_depth), root

        _, node = dfs(root)
        return node