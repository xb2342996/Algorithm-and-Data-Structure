## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode
'''
给定一个二叉树，编写一个函数来获取这个树的最大宽度。
树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
'''


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        queue.append((root, 0, 0))
        current_depth = 0
        left_pos = 0
        ans = 0
        while queue:
            node, depth, pos = queue.pop()
            if node.left:
                queue.append((node.left, depth + 1, 2 * pos))
            if node.right:
                queue.append((node.right, depth + 1, 2 * pos + 1))
            if depth != current_depth:
                current_depth = depth
                left_pos = pos
            ans = max(ans, pos - left_pos + 1)
        return ans


    # def widthOfBinaryTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     queue = []
    #     queue.append(root)
    #     trees = []
    #     level = []
    #     count = 1
    #     height = self.height(root)
    #     while queue and len(trees) <= height:
    #         node = queue.pop(0)
    #         count -= 1
    #         level.append(node.val)
    #         if count == 0:
    #             trees.append(level)
    #             count = len(queue)
    #             level = []
    #
    #         if node.left:
    #             queue.append(node.left)
    #         else:
    #             queue.append(TreeNode(None))
    #
    #         if node.right:
    #             queue.append(node.right)
    #         else:
    #             queue.append(TreeNode(None))
    #     width = 0
    #     for t in trees:
    #         while t[0] is None:
    #             t.pop(0)
    #         while t[-1] is None:
    #             t.pop()
    #         width = max(width, len(t))
    #     return width

    # def height(self, node):
    #     if node is None:
    #         return 0
    #     return 1 + max(self.height(node.left), self.height(node.right))