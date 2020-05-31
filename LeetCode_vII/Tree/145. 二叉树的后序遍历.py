## written by xiongbiao
## date 2020-5-31
from Tree.node import TreeNode

'''
给定一个二叉树，返回它的 后序 遍历。
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.output = []
        self.postorder(root)
        return self.output

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        self.output.append(node.val)
    '''
    迭代法 空间复杂度O（n）时间复杂度O（n）
    '''
    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root is None:
    #             return []
    #
#         stack1 = []
#         stack2 = []
#         stack1.append(root)
#         while stack1:
#             node = stack1.pop()
#             stack2.append(node.val)
#             if node.left:
#                 stack1.append(node.left)
#             if node.right:
#                 stack1.append(node.right)
#
#         return stack2[::-1]

Solution()