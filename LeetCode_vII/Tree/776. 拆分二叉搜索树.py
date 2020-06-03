## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
给你一棵二叉搜索树（BST）、它的根结点 root 以及目标值 V。
'''
class Solution(object):
    '''
    递归遍历一条从根节点到叶子节点的路径将路径中小于目标值的与大于目标值的节点分离
    '''
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root is None:
            return [None, None]

        elif root.val <= V:
            bns = self.splitBST(root.right, V)
            root.right = bns[0]
            return root, bns[1]
        else:
            bns = self.splitBST(root.left, V)
            root.left = bns[1]
            return bns[0], root



