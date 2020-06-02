## written by xiongbiao
## date 2020-6-2

from Tree.node import TreeNode
'''
给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。
添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。
'''
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        prev_level = []
        next_level = []

        queue = []
        queue.append(root)
        count = 1
        level = 1
        while queue:
            node = queue.pop(0)
            if level == d - 1:
                prev_level.append(node)
            if level == d:
                next_level.append(node)
            count -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if count == 0:
                count = len(queue)
                level += 1
            if level == d + 1:
                break

        while len(prev_level) > 0:
            node = prev_level.pop(0)

            if next_level[0] == node.left:
                new_node = TreeNode(v)
                left = next_level.pop(0)
                new_node.left = left
                node.left = new_node
            if next_level[0] == node.right:
                new_node = TreeNode(v)
                right = next_level.pop(0)
                new_node.right = right
                node.right = new_node

