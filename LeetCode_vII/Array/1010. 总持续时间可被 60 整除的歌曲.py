"""
@author: xiongbiao
@date: 2021-05-23 22:31
"""
'''
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
'''

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import defaultdict
        map = defaultdict(int)
        count = 0
        for t in time:
            mod_val = t % 60
            if mod_val == 0:
                remainder = 0
            else:
                remainder = 60 - mod_val
            count += map[remainder]
            map[mod_val] += 1
        return count

