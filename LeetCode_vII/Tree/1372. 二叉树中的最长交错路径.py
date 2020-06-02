## written by xiongbiao
## date 2020-6-2
from Tree.node import TreeNode

'''
给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：
选择二叉树中 任意 节点和一个方向（左或者右）。
如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
改变前进方向：左变右或者右变左。
重复第二步和第三步，直到你在树中无法继续移动。
'''

class Solution(object):
    '''
    一次遍历，深度遍历如果上一次方向是左，这次方向是右继续深度遍历，同时重置左方向的路径长度为1，继续深度遍历左侧
    '''
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = 0
        self.zigzag(root, 0, True)
        return self.max_path

    def zigzag(self, node, path, direction):
        if node is None:
            self.max_path = max(self.max_path, path - 1)
            return
        if direction:
            self.zigzag(node.right, path + 1, not direction)
            self.zigzag(node.left, 1, direction)
        else:
            self.zigzag(node.left, path + 1, not direction)
            self.zigzag(node.right, 1, direction)

    '''
    广度遍历每个节点，对每个节点执行左方向zigzag深度遍历
    '''
    # def longestZigZag(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     self.max_path = 0
    #     queue = []
    #     queue.append(root)
    #     while queue:
    #         node = queue.pop(0)
    #         # left = True right = False
    #         self.zigzag(node.left, 0, True)
    #         self.zigzag(node.right, 0, False)
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     return self.max_path
    #
    # def zigzag(self, node, path, direction):
    #     if node is None:
    #         self.max_path = max(path, self.max_path)
    #         return
    #     if direction:
    #         self.zigzag(node.right, path + 1, not direction)
    #     else:
    #         self.zigzag(node.left, path + 1, not direction)