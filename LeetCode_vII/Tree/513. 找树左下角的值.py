## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个二叉树，在树的最后一行找到最左边的值。
'''
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        queue = [root]
        count = 1
        next_level = True
        ans = root.val
        while queue:
            node = queue.pop(0)
            if next_level:
                ans = node.val
                next_level = False
            count -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if count == 0:
                count = len(queue)
                next_level = True
        return ans
