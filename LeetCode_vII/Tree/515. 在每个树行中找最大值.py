## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
您需要在二叉树的每一行中找到最大的值。
'''

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = []
        queue = [root]
        count = 1
        max_val = float('-inf')
        while queue:
            node = queue.pop(0)
            count -= 1
            max_val = max(max_val, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if count == 0:
                count = len(queue)
                ans.append(max_val)
                max_val = float('-inf')
        return ans