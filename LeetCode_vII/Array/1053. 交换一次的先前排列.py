"""
@author: xiongbiao
@date: 2021-06-01 21:59
"""

'''
给你一个正整数的数组 A（其中的元素不一定完全不同），请你返回可在 一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的、按字典序排列小于 A 的最大可能排列。
如果无法这么操作，就请返回原数组。
'''

class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        length = len(arr)
        max_val = -1
        max_index = -1
        flag = False
        for i in range(length - 2, -1, -1):
            if arr[i] > arr[i+1]:
                for j in range(i+1, length):
                    if arr[i] > arr[j]:
                        flag = True
                        if arr[j] > max_val:
                            max_val = arr[j]
                            max_index = j
                if flag:
                    arr[i], arr[max_index] =  max_val, arr[i]
                    return arr

        return arr




print(Solution().prevPermOpt1([3,1,1,3]))