"""
@author: xiongbiao
@date: 2021-04-25 21:28
"""
'''
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。
返回 A 的任意排列，使其相对于 B 的优势最大化。
'''
'''
解题思路：
田忌赛马，重点在于利用数据结构的特点去简化代码操作，使用deque从头部和尾部弹出数字，映射Map对应关系
'''

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        from collections import deque
        A = sorted(A)
        Bs = deque(sorted(B))
        assign = {b: [] for b in B}

        for a in A:
            if a > Bs[0]:
                assign[Bs[0]].append(a)
                Bs.popleft()
            else:
                assign[Bs[-1]].append(a)
                Bs.pop()

        return [assign[b].pop() for b in B]


Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11])