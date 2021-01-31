# written by xiong biao
# date 2020 1 6

'''
假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
在每一步操作中，你可以选择任意 m （1 ≤ m ≤ n） 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数。如果不能使每台洗衣机中衣物的数量相等，则返回 -1。
'''

class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """

        total = sum(machines)
        if total % len(machines) != 0:
            return -1
        mean = (int)(total / len(machines))
        diff = []
        for n in machines:
            diff.append(n - mean)
        print(diff)
        res = 0
        curr_sum, max_sum = 0, 0
        for d in diff:
            curr_sum += d
            max_sum = max(max_sum, abs(curr_sum))
            res = max(max_sum, res, d)

        return res

print(Solution().findMinMoves([0, 3, 0]))