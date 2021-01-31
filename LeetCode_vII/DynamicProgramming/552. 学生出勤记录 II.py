"""
@author: xiongbiao
@date: 2021-01-10 10:58
"""

'''
给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。
学生出勤记录是只包含以下三个字符的字符串：
'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的
'''
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 10 ** 9 + 7

        a0l0 = 1
        a0l1, a0l2, a1l0, a1l1, a1l2 = 0, 0, 0, 0, 0
        for i in range(n + 1):
            a0l0_ = (a0l0 + a0l1 + a0l2) % m

            a0l2 = a0l1
            a0l1 = a0l0
            a0l0 = a0l0_

            a1l0_ = (a0l0 + a1l0 + a1l1 + a1l2) % m
            a1l2 = a1l1
            a1l1 = a1l0
            a1l0 = a1l0_

        return a1l0

