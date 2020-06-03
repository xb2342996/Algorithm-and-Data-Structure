## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

行数 m 应当等于给定二叉树的高度。
列数 n 应当总是奇数。
根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。
根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。
你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。
即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。
然而，如果两个子树都为空则不需要为它们留出任何空间。
每个未使用的空间应包含一个空的字符串""。
使用相同的规则输出子树。
'''
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.height(root)
        width = (2 ** height) - 1
        tree = [[''] * width for _ in range(height)]

        queue = []
        queue.append(root)
        count = 1
        level = 0
        left, right = 0, width
        interval = (left + right) / (2 ** level)
        while queue and level < height:
            node = queue.pop(0)
            count -= 1
            index = left + int(interval / 2)
            if node.val is not None:
                tree[level][index] = str(node.val)
            left += interval + 1
            if node.left:
                queue.append(node.left)
            else:
                queue.append(TreeNode(None))
            if node.right:
                queue.append(node.right)
            else:
                queue.append(TreeNode(None))

            if count == 0:
                level += 1
                left = 0
                count = len(queue)
                if count != 0:
                    interval = (left + right) / (2 ** level)
        return tree

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))