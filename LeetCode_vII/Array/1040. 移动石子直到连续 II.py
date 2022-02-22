"""
@author: xiongbiao
@date: 2021-05-30 22:40
"""

'''
在一个长度 无限 的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作 端点石子 。
每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。
值得注意的是，如果石子像 stones = [1,2,5] 这样，你将 无法 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该石子都仍然会是端点石子。
当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves] 。
'''

class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        l = len(stones)
        max_val = max(stones)
        min_val = min(stones)
        m = [0] * (max_val + 1)
        for s in stones:
            m[s] = 1
        print(m)
        p, q = min_val, min_val + l
        count = 0
        for s in range(p, q - 1):
            if m[s] == 1:
                count += 1

        if count == l:
            return [0, 0]

        max_m = max(0, count)
        min_m = min(float('inf'), count)
        while q < max_val + 1:
            if m[q] == 1 and m[p] == 0:
                count += 1
            elif m[q] == 0 and m[p] == 1:
                count -= 1
            max_m = max(max_m, count)
            min_m = min(min_m, count)
            q += 1
            p += 1

        print(l - max_m, l - min_m)



Solution().numMovesStonesII([6,5,4,3,10])
