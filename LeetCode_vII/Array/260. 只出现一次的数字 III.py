"""
@author: xiongbiao
@date: 2021-08-25 23:07
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        011
        101
        110
        """
        ret = 0
        for n in nums:
            ret ^= n
            print(ret)

        div = 1
        while div & ret == 0:
            div <<= 1
        print(div)
        one, two = 0, 0
        for n in nums:
            if div & n != 0:
                one ^= n
            else:
                two ^= n
        return [one, two]


Solution().singleNumber([1,2,1,3,2,5])