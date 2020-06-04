## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
'''
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        return self.preorder(preorder, 0, len(preorder) - 1)

    def preorder(self, preorder, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(preorder[left])

        root = TreeNode(preorder[left])
        index = left
        while index + 1 <= right and preorder[index + 1] < preorder[left]:
            index += 1

        root.left = self.preorder(preorder, left + 1, index)
        root.right = self.preorder(preorder, index + 1, right)
        return root

preorder = [4, 2]
print(preorder[1:])