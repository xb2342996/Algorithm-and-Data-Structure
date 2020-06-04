## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
'''

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = []
        queue = [root]
        count = 1
        while queue:
            node = queue.pop(0)
            count -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if count == 0:
                ans.append(node.val)
                count = len(queue)

        print(ans)
        return ans
