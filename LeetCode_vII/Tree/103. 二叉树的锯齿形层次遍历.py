## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode

'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
'''
class Solution(object):

    '''
    DFS
    '''
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        results = []
        def dfs(node, level):
            if level >= len(results):
                results.append([node.val])
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].insert(0, node.val)

            for child in [node.left, node.right]:
                if child:
                    dfs(child, level + 1)

        dfs(root, 0)
        return results
    '''
    BFS 
    '''
    # def zigzagLevelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     if root is None:
    #         return []
    #
    #     ans, level = [], []
    #     count = 1
    #     direction = True
    #     stack1, stack2 = [], []
    #     stack1.append(root)
    #
    #     while stack1 or stack2:
    #         if direction:
    #             node = stack1.pop()
    #             count -= 1
    #             if node.left:
    #                 stack2.append(node.left)
    #             if node.right:
    #                 stack2.append(node.right)
    #         else:
    #             node = stack2.pop()
    #             count -= 1
    #             if node.right:
    #                 stack1.append(node.right)
    #             if node.left:
    #                 stack1.append(node.left)
    #         level.append(node.val)
    #         if count == 0:
    #             direction = not direction
    #             count = len(stack1) if stack1 else len(stack2)
    #             ans.append(level[:])
    #             level = []


