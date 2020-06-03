## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
对于一棵深度小于 5 的树，可以用一组三位十进制整数来表示。
对于每个整数：
百位上的数字表示这个节点的深度 D，1 <= D <= 4。
十位上的数字表示这个节点在当前层所在的位置 P， 1 <= P <= 8。位置编号与一棵满二叉树的位置编号相同。
个位上的数字表示这个节点的权值 V，0 <= V <= 9。
给定一个包含三位整数的升序数组，表示一棵深度小于 5 的二叉树，请你返回从根到所有叶子结点的路径之和。
'''
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ans = 0
        values = {x // 10: x % 10 for x in nums}
        def dfs(node, sum=0):
            if node not in values:
                return
            sum += values[node]
            depth = node // 10
            level = node % 10
            left = 10 * (depth + 1) + 2 * level - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += sum
            else:
                dfs(left, sum)
                dfs(right, sum)

        dfs(11)
        return self.ans




print(Solution().pathSum([113, 215, 221]))