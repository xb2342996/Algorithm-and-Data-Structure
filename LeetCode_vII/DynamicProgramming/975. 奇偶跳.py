"""
@author: xiongbiao
@date: 2021-02-21 17:38
"""
'''
给定一个整数数组 A，你可以从某一起始索引出发，跳跃一定次数。在你跳跃的过程中，第 1、3、5... 次跳跃称为奇数跳跃，而第 2、4、6... 次跳跃称为偶数跳跃。
你可以按以下方式从索引 i 向后跳转到索引 j（其中 i < j）：
在进行奇数跳跃时（如，第 1，3，5... 次跳跃），你将会跳到索引 j，使得 A[i] <= A[j]，A[j] 是可能的最小值。如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
在进行偶数跳跃时（如，第 2，4，6... 次跳跃），你将会跳到索引 j，使得 A[i] >= A[j]，A[j] 是可能的最大值。如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
（对于某些索引 i，可能无法进行合乎要求的跳跃。）
如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 A.length - 1），那么该索引就会被认为是好的起始索引。
返回好的起始索引的数量。
'''

class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)

        def processor(m):
            ans = [None] * len(m)
            stack = []
            for i in m:
                while stack and stack[-1] < i:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(n), key=lambda i: A[i])
        odd_next = processor(B)
        B = sorted(range(n), key=lambda i: -A[i])
        even_next = processor(B)

        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True

        for i in range(n - 2, -1, -1):
            if odd_next[i] is not None:
                odd[i] = even[odd_next[i]]
            if even_next[i] is not None:
                even[i] = odd[even_next[i]]
        return sum(odd)



Solution().oddEvenJumps([2,3,1,1,4])