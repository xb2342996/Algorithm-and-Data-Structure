## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = [root]
        ans, level = [], []
        count = 1
        while queue:
            node = queue.pop(0)
            level.append(node.val)
            count -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if count == 0:
                count = len(queue)
                ans.append(level)
                level = []
        return ans

