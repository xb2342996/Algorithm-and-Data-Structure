"""
@author: xiongbiao
@date: 2021-01-31 22:19
"""
'''
给你一个数组 nums 表示 1 到 n 的一个排列。我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉查找树（BST）。请你统计将 nums 重新排序后，统计满足如下条件的方案数：重排后得到的二叉查找树与 nums 原本数字顺序得到的二叉查找树相同。
比方说，给你 nums = [2,1,3]，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。数组 [2,3,1] 也能得到相同的 BST，但 [3,2,1] 会得到一棵不同的 BST 。
请你返回重排 nums 后，与原数组 nums 得到相同二叉查找树的方案数。
由于答案可能会很大，请将结果对 10^9 + 7 取余数。
'''

class Solution(object):
    def __init__(self):
        self.mod = 10 ** 9 + 7

    def numOfWays(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        limit = max(nums)
        self.dp = [[0] * (limit + 1) for _ in range(limit + 1)]
        for i in range(limit + 1):
            for j in range(limit + 1):
                if j == 0:
                    self.dp[i][j] = 1
                else:
                    self.dp[i][j] = (self.dp[i-1][j-1] + self.dp[i-1][j]) % self.mod
        return (self.dfs(nums) - 1) % self.mod


    def dfs(self, sub_tree):
        if len(sub_tree) == 0:
            return 1
        left, right = [], []
        root = sub_tree[0]
        for i in range(1, len(sub_tree)):
            if sub_tree[i] > root:
                right.append(sub_tree[i])
            else:
                left.append(sub_tree[i])

        return (self.dp[len(sub_tree)-1][len(left)] * self.dfs(left) % self.mod * self.dfs(right)) % self.mod

print(Solution().numOfWays([3,4,5,1,2]))
